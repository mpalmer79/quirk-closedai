import os
from fastapi import FastAPI
from pydantic import BaseModel
from src.utils.prompt_loader import Prompts


# If you use an OpenAI‑compatible local gateway, expose it via env vars
OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL", "http://localhost:8001/v1")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "changeme")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-5")


from openai import OpenAI
client = OpenAI(base_url=OPENAI_BASE_URL, api_key=OPENAI_API_KEY)


app = FastAPI()
prompts = Prompts()


class ChatRequest(BaseModel):
message: str
department: str | None = None
model: str | None = None


@app.get("/health")
def health():
return {"status": "ok"}


@app.post("/chat")
def chat(req: ChatRequest):
system_text = prompts.compose(req.department)
messages = [
{"role": "system", "content": system_text},
{"role": "user", "content": req.message},
]
model = req.model or MODEL_NAME
resp = client.chat.completions.create(model=model, messages=messages)
return {"output": resp.choices[0].message.content}
