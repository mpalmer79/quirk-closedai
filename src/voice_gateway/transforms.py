# Stubs for where you'll call OpenAI STT/TTS or the Realtime API.
# Keep here so the server can import without errors during early tests.

async def stt_to_text(audio_base64: str) -> str:
    # TODO: implement with OpenAI STT if you need server-side transcription
    return "[transcript omitted in stub]"

async def text_to_tts(text: str) -> bytes:
    # TODO: implement with OpenAI TTS, return raw audio bytes (PCM or μ-law)
    return b""

