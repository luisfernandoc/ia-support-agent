# app/chains.py
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from .config import get_env

PROMPT = ChatPromptTemplate.from_template(
    """You are a concise, helpful AI support agent.
Use the provided CONTEXT first; if it doesn't contain the answer, say you don't know and give a short, safe suggestion.

CONTEXT:
{context}

User: {question}
Assistant:"""
)

def build_chain(temperature: float = 0.2):
    llm = ChatOpenAI(
        api_key=get_env("OPENAI_API_KEY"),
        model=get_env("MODEL_NAME", "gpt-4o-mini"),
        temperature=temperature,
        timeout=30,
    )
    return (PROMPT | llm)
