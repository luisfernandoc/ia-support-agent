# app/stores.py
from sqlalchemy import create_engine, text
from .config import get_env

DATABASE_URL = get_env("DATABASE_URL", "sqlite:///./agent.db")
engine = create_engine(DATABASE_URL, future=True)

def init_db():
    with engine.begin() as conn:
        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS chat_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_text TEXT,
            context TEXT,
            reply TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )"""))

def log_interaction(user_text: str, context: str, reply: str):
    with engine.begin() as conn:
        conn.execute(
            text("INSERT INTO chat_history (user_text, context, reply) VALUES (:u, :c, :r)"),
            {"u": user_text, "c": context, "r": reply}
        )
