FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy only the gateway code (adjust paths if your repo differs)
COPY src/voice_gateway /app/src/voice_gateway
COPY config /app/config

EXPOSE 8080
CMD ["uvicorn", "src.voice_gateway.server:app", "--host", "0.0.0.0", "--port", "8080"]
