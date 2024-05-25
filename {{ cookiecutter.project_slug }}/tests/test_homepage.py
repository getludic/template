from starlette.testclient import TestClient

from src.main import app


def test_bulk_update() -> None:
    with TestClient(app) as client:
        response = client.get("/")

        assert response.status_code == 200
        assert b"Hello" in response.content
