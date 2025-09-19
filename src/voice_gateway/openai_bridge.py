import os, json, asyncio, websockets

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
REALTIME_MODEL = os.getenv("OPENAI_REALTIME_MODEL", "gpt-realtime-preview")

class OpenAIRealtimeBridge:
    """
    Minimal helper around OpenAI Realtime over WebSocket.
    You will forward PCM/μ-law frames in, and receive synthesized audio/text out.
    """
    def __init__(self, system_prompt: str):
        self._prompt = system_prompt
        self._ws = None

    async def connect(self):
        # NOTE: endpoint/name may differ for your contract — adjust accordingly.
        url = f"wss://api.openai.com/v1/realtime?model={REALTIME_MODEL}"
        self._ws = await websockets.connect(
            url,
            extra_headers={
                "Authorization": f"Bearer {OPENAI_API_KEY}",
                "OpenAI-Beta": "realtime=v1"
            },
            max_size=None,
        )
        # Set system prompt
        await self._ws.send(json.dumps({
            "type": "session.update",
            "session": {"instructions": self._prompt}
        }))

    async def send_audio_chunk(self, pcm_bytes: bytes, sample_rate_hz: int = 8000):
        """
        Send an audio chunk to the realtime session.
        """
        if not self._ws: return
        await self._ws.send(json.dumps({
            "type": "input_audio_buffer.append",
            "audio": pcm_bytes.decode("latin1"),   # raw bytes in compat form
            "sample_rate": sample_rate_hz
        }))

    async def commit_input(self):
        if not self._ws: return
        await self._ws.send(json.dumps({"type": "input_audio_buffer.commit"}))
        await self._ws.send(json.dumps({"type": "response.create"}))

    async def next_event(self):
        """
        Await next event from the model (text/audio tokens, etc.)
        """
        if not self._ws: return None
        msg = await self._ws.recv()
        try:
            return json.loads(msg)
        except Exception:
            return {"type": "binary", "data": msg}

    async def close(self):
        if self._ws:
            await self._ws.close()
            self._ws = None
