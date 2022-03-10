from app.main import app
from starlette.testclient import TestClient

client = TestClient(app)


def test_ping(test_app):
    response = test_app.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"ping": "pong!"}
