
### docs/voice/security.md
```markdown
# Security & Data Handling
- Edge redaction: mask names, emails, VINs (last 8 only) before sending to model.
- Logs: metadata only (timestamps, route, intent, token counts).
- OpenAI API: business data not used for training by default; request ZDR if needed.  
Refs: Enterprise privacy / business data.  

