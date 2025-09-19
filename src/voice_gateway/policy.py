import re

# Very simple redaction stub — expand later
VIN_RE = re.compile(r"\b([A-HJ-NPR-Z0-9]{17})\b", re.I)
EMAIL_RE = re.compile(r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}", re.I)
PHONE_RE = re.compile(r"\+?\d[\d\-\s()]{8,}\d")

def redact(text: str) -> str:
    text = VIN_RE.sub(lambda m: f"{m.group(0)[:9]}********", text)  # keep first 9, mask rest
    text = EMAIL_RE.sub("[redacted_email]", text)
    text = PHONE_RE.sub("[redacted_phone]", text)
    return text

