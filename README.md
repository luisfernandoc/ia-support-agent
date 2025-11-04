Objetivo: Agente de soporte IA con FastAPI + LangChain + OpenAI, retrieval local (CSV/SQLite), y webhook estilo WhatsApp.

Adaptable a OyeCompa:

Webhook /whatsapp/webhook + capa LLM desacoplada (llm.py).

DevSerper opcional para grounding/búsqueda.

Adaptable a CCRen:

Arquitectura modular de “AI Agent Engineer” (LLM + retrieval + logs + endpoints).

Fácil de expandir a tool-use y agentes (LangChain Tools).

Seguridad: variables en .env, sin claves embebidas.

Escalabilidad: Dockerfile, separación de capas, logs para métricas.

Comandos de demo (rápido):

curl -s http://localhost:8000/health
curl -s -X POST http://localhost:8000/chat -H "Content-Type: application/json" \
  -d '{"message":"Do you support WhatsApp?"}'
curl -s -X POST http://localhost:8000/whatsapp/webhook -H "Content-Type: application/json" \
  -d '{"from_id":"555123","text":"How do I reset my password?"}'