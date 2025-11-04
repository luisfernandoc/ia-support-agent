from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_chat():
    r = client.post("/chat", json={"message":"How do I reset my password?"})
    assert r.status_code == 200
    assert "reply" in r.json()
