import httpx
from ..config import DEVSERPER_API_KEY

async def web_search(q: str) -> str:
    """Búsqueda simple con DevSerper (si hay API key)."""
    if not DEVSERPER_API_KEY:
        return ""
    url = "https://google.serper.dev/search"
    headers = {"X-API-KEY": DEVSERPER_API_KEY, "Content-Type": "application/json"}
    payload = {"q": q, "num": 3}
    async with httpx.AsyncClient(timeout=10) as client:
        r = await client.post(url, headers=headers, json=payload)
        r.raise_for_status()
        data = r.json()
        snippets = []
        for item in data.get("organic", [])[:3]:
            snippets.append(f"{item.get('title','')}: {item.get('snippet','')}")
        return "\n".join(snippets)
