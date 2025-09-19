import asyncio, json, os
from fastapi import FastAPI, WebSocket
from fastapi.responses import PlainTextResponse
from policy import redact
from transforms import stt_to_text, text_to_tts

app = FastAPI()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

@app.get("/health")
def health():
    return PlainTextResponse("ok")

@app.websocket("/realtime")
async def realtime(ws: WebSocket):
    await ws.accept()
    # In production: bridge PBX/Twilio media here, send to OpenAI Realtime over WebRTC/WS.
    # Pseudocode event loop:
    while True:
        msg = await ws.receive_text()
        data = json.loads(msg)
        if data.get("type") == "audio.chunk":
            # 1) STT (or forward chunk to Realtime session)
            text = await stt_to_text(data["payload"])
            safe = redact(text)
            # 2) Send to OpenAI Realtime (omitted: session mgmt)
            # 3) Receive model response text -> TTS -> stream back
            audio = await text_to_tts("Thanks for calling Quirk! " + safe)
            await ws.send_bytes(audio)

