# app/retrieval.py
import pandas as pd
from typing import List

class SimpleCSVRetriever:
    def __init__(self, path: str):
        self.df = pd.read_csv(path)  # columnas: question, answer

    def search(self, query: str, k: int = 3) -> List[str]:
        q = query.lower().split()
        scored = []
        for _, row in self.df.iterrows():
            blob = f"{row.get('question','')} {row.get('answer','')}".lower()
            score = sum(t in blob for t in q)
            scored.append((score, row.get("answer", "")))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [ans for score, ans in scored[:k] if score > 0]
