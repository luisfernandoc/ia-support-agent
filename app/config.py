# app/config.py
import os
from pathlib import Path
from dotenv import load_dotenv

# Ruta absoluta al .env en la raíz del proyecto
DOTENV_PATH = Path(__file__).resolve().parents[1] / ".env"
load_dotenv(dotenv_path=DOTENV_PATH, override=True)

def get_env(name: str, default: str = "") -> str:
    return os.getenv(name, default)
