from starlette.testclient import TestClient
from main import app

client = TestClient(app)


def test_Invalid_post_status_code():
    response = client.post("/wishlist")
    assert response.status_code == 422


def test_read_inexistent_item():
    response = client.get("/whishlist/bola")
    assert response.status_code == 404
    assert response.json == {"detail": "Item not found"}


# data = {
#     "presente1": {"id": 3, "name": "PresenteA", "description": "somente um teste", "image": "", "link": "", "have": False}

# def test_valid_post_status_code():
#     response = client.post("/wishlist", data)
#     assert response.status_code == 201
