# Quirk AI Voice — Overview
Goal: corporate-managed, on-prem voice assistant that answers, routes, and resolves common sales/service requests across all Quirk rooftops.

## High-level flow
```mermaid
sequenceDiagram
  participant Caller
  participant PBX as PBX/SIP or Twilio
  participant GW as Quirk Voice Gateway (on-prem)
  participant OAI as OpenAI Realtime API
  participant Human as Store Agent

  Caller->>PBX: Inbound call
  PBX->>GW: Audio (SIP/RTP or Media Stream)
  GW->>OAI: Bidirectional audio + events (realtime)
  OAI-->>GW: Tokens + speech
  GW-->>PBX: TTS audio back to caller
  alt low confidence / requested transfer
    GW->>Human: Warm transfer
  end

