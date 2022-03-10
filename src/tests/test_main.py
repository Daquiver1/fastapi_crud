from pydoc import resolve

from app.main import app
from starlette.testclient import TestClient

client = TestClient(app)


def test_ping():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"ping": "pong!"}
