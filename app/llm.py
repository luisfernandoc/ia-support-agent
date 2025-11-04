from langchain_openai import ChatOpenAI
from .config import OPENAI_API_KEY, MODEL_NAME

def get_llm(temperature: float = 0.2):
    # Abstracción simple para swapear proveedor si hace falta
    return ChatOpenAI(
        api_key=OPENAI_API_KEY,
        model=MODEL_NAME,
        temperature=temperature,
        timeout=30,
    )
