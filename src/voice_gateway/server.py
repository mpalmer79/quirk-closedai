import os, json, asyncio, base64
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import PlainTextResponse
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

# env vars (populate in .env at deploy time, don't commit real values)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "set-me")
REALTIME_MODEL = os.getenv("REALTIME_MODEL", "realtime-model-name")
SYSTEM_PROMPT_PATH = os.getenv("SYSTEM_PROMPT_PATH", "config/prompts/voice_system.md")

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
    This endpoint is designed for a Twilio <Connect><Stream> bidirectional media stream.
    For the pilot: we just accept the stream and log message types so you can verify end-to-end routing.
    Later, bridge to OpenAI Realtime (WebRTC/WS) and stream TTS back.
    """
    await ws.accept()
    system_prompt = load_system_prompt()
    print("[WS] connected; prompt bytes:", len(system_prompt))

    try:
        while True:
            msg = await ws.receive_text()
            data = json.loads(msg)
            event_type = data.get("event", data.get("type"))
            if event_type in ("start", "connected"):
                print(f"[WS] {event_type}: {data}")
            elif event_type == "media":
                # Twilio sends 20ms PCM frames base64-encoded in data['media']['payload']
                # payload = base64.b64decode(data["media"]["payload"])
                pass
            elif event_type in ("stop", "close"):
                print(f"[WS] stop: {data}")
                break
            else:
                print(f"[WS] other: {data.keys()}")
    except WebSocketDisconnect:
        print("[WS] disconnected")
    except Exception as e:
        print("[WS] error:", e)
    finally:
        await ws.close()
