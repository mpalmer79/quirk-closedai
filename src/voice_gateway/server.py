import os, json, asyncio, base64
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import PlainTextResponse
from dotenv import load_dotenv

from .policy import redact
from .audio_utils import decode_twilio_payload, mulaw_to_pcm, resample_pcm16
from .openai_bridge import OpenAIRealtimeBridge

load_dotenv()
app = FastAPI()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
REALTIME_MODEL = os.getenv("OPENAI_REALTIME_MODEL", "gpt-realtime-preview")
SYSTEM_PROMPT_PATH = os.getenv("SYSTEM_PROMPT_PATH", "config/prompts/voice_system.md")
BIDI = os.getenv("BIDIRECTIONAL_STREAMS", "true").lower() == "true"

def load_system_prompt():
    try:
        with open(SYSTEM_PROMPT_PATH, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "You are Quirk AI Voice."

@app.get("/health")
def health():
    return PlainTextResponse("ok")

@app.websocket("/realtime/twilio")
async def twilio_stream(ws: WebSocket):
    """
    Twilio <Connect><Stream> handler.

    Twilio events:
      - start: streamSid, callSid
      - media: 20ms chunks, b64 payload (μ-law or PCM)
      - stop:  end of stream

    We forward inbound audio to OpenAI Realtime, and (when enabled/available)
    stream synthesized audio back to Twilio (bidirectional).
    """
    await ws.accept()
    prompt = load_system_prompt()

    # Bridge to OpenAI
    oai = OpenAIRealtimeBridge(system_prompt=prompt)
    await oai.connect()

    try:
        while True:
            msg = await ws.receive_text()
            data = json.loads(msg)
            evt = data.get("event") or data.get("type")

            if evt == "start":
                print("[twilio] start:", data.get("start", {}))
                continue

            if evt == "media":
                payload = data["media"]["payload"]
                raw = decode_twilio_payload(payload)       # μ-law or PCM
                pcm16 = mulaw_to_pcm(raw)                  # convert μ-law → PCM16
                pcm16 = resample_pcm16(pcm16, 8000, 16000) # 8k → 16k for model comfort

                # Send audio to the model (non-blocking)
                await oai.send_audio_chunk(pcm16, sample_rate_hz=16000)
                continue

            if evt == "mark":
                continue

            if evt == "stop":
                print("[twilio] stop")
                break

    except WebSocketDisconnect:
        print("[twilio] client disconnected")
    except Exception as e:
        print("[twilio] error:", e)
    finally:
        try:
            await oai.commit_input()
        except Exception:
            pass
        await oai.close()
        await ws.close()
