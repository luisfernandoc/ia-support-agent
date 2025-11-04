# app/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Importa config primero para que cargue el .env
from . import config  # ← importante: carga el .env
from .chains import build_chain
from .retrieval import SimpleCSVRetriever
from .stores import init_db, log_interaction

app = FastAPI(title="AI Support Agent")

retriever = SimpleCSVRetriever("data/faqs.csv")
chain = build_chain()
init_db()

@app.get("/health")
def health():
    return {"status": "ok"}

class ChatIn(BaseModel):
    message: str
    use_web: bool = False

class WhatsAppMsg(BaseModel):
    from_id: str
    text: str

@app.post("/chat")
async def chat(payload: ChatIn):
    import os
    if not os.getenv("OPENAI_API_KEY"):
        raise HTTPException(status_code=500, detail="OPENAI_API_KEY not set")

    q = payload.message.strip()
    if not q:
        raise HTTPException(400, "Empty message")

    hits = retriever.search(q, k=3)
    context = "\n".join(hits) if hits else ""
    resp = await chain.ainvoke({"question": q, "context": context})
    reply = getattr(resp, "content", str(resp))
    log_interaction(q, context, reply)
    return {"reply": reply}

@app.post("/whatsapp/webhook")   # <--- ESTA ES LA RUTA QUE FALTA
async def whatsapp_webhook(msg: WhatsAppMsg):
    q = msg.text.strip()
    hits = retriever.search(q, k=3)
    context = "\n".join(hits) if hits else ""
    resp = await chain.ainvoke({"question": q, "context": context})
    reply = getattr(resp, "content", str(resp))
    log_interaction(q, context, reply)
    # En integración real, aquí llamarías a la API de WhatsApp para enviar 'reply'
    return {"to": msg.from_id, "reply": reply}
