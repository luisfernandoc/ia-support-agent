# 🤖 AI Support Agent

An intelligent support assistant built with **FastAPI**, **LangChain**, and **OpenAI GPT-4o**.  
It supports REST endpoints for chat and WhatsApp-style webhooks, uses a local FAQ CSV file for retrieval, and logs all interactions in SQLite.

---


## 🚀 Features
- **Chat endpoint** for AI responses
- **WhatsApp webhook** simulation
- **Retrieval-Augmented Generation (RAG)** over `data/faqs.csv`
- **SQLite logging** for all user messages
- Modular design for future integrations (e.g., FAISS, Postgres, Docker)

---


## ⚙️ Installation

```bash
git clone https://github.com/luisfernandoc/ai-support-agent.git
cd ai-support-agent
python -m venv .venv
.venv\Scripts\activate   # (Windows)
pip install -r requirements.txt
cp .env.example .env
```


## 🚀 Edit .env and set your OpenAI key:

```bash
OPENAI_API_KEY=sk-xxxx
MODEL_NAME=gpt-4o-mini
DATABASE_URL=sqlite:///./agent.db
```


## ▶️ Run locally

```bash
python -m uvicorn app.main:app --reload
```
Visit → http://127.0.0.1:8000/docs


## 💬 Example API calls

```bash
# Health check
Invoke-RestMethod http://127.0.0.1:8000/health

# Chat
Invoke-RestMethod -Uri "http://127.0.0.1:8000/chat" -Method POST -ContentType "application/json" -Body '{"message":"Hello!"}'
```


## 🧠 Tech Stack

- Python 3.13
- FastAPI
- LangChain + OpenAI
- Pandas
- SQLAlchemy
- Uvicorn
- dotenv

## 👨‍💻 Author

Luis Fernando Cuevas Álvarez
