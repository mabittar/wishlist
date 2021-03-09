from starlette.testclient import TestClient
from app.server.app import app, wishlist

client = TestClient(app)


def test_invalid_post_status_code():
    response = client.post("/wishlist")
    assert response.status_code == 422


def test_read_inexistent_item():
    response = client.get("/whishlist/bola")
    assert response.status_code == 404

