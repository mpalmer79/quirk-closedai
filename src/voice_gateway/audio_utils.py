import base64, numpy as np

def decode_twilio_payload(b64_payload: str) -> bytes:
    """Twilio media.payload → raw bytes (usually μ-law 8kHz mono)."""
    return base64.b64decode(b64_payload)

def mulaw_to_pcm(mu: bytes) -> bytes:
    """
    Very small μ-law → PCM16 converter.
    If your Twilio stream is PCM already, just return as-is.
    """
    # μ-law table approach (fast enough for pilot)
    import audioop
    return audioop.ulaw2lin(mu, 2)  # 16-bit linear PCM

def resample_pcm16(pcm: bytes, src_rate: int = 8000, dst_rate: int = 16000) -> bytes:
    """Naive resample (zero-order hold) for pilot only. Replace with SoX/libsamplerate later."""
    if src_rate == dst_rate:
        return pcm
    import audioop
    return audioop.ratecv(pcm, 2, 1, src_rate, dst_rate, None)[0]
