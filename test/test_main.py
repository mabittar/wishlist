from schemas import WISHES, Wish, fake_wish_db
from starlette.testclient import TestClient
from copy import copy
from main import app

DEFAULT_WISH = Wish(id=1, name="mouse", description="mouse sem fio",
                    image_link="https://www.corsair.com/corsairmedia/sys_master/productcontent/ch-9315311-na-dark_core_rgb_se_04.png",
                    link="https://www.corsair.com/br/pt/Categorias/Produtos/Mouses-gamer/Wireless-Gaming-Mice/DARK-CORE-RGB-PRO-SE-Wireless-Gaming-Mouse/p/CH-9315511-NA",
                    have=False)

RESP = TestClient(app).get("/wishlist")


def test_listing_wishes_should_return_200():
    assert RESP.status_code == 200


def test_listing_wishes_should_return_json():
    assert RESP.headers["Content-Type"] == "application/json"


def test_listing_wishlist_should_return_list():
    assert isinstance(RESP.json(), list)


def test_listing_wishes_return_one_wish_with_id():
    WISHES.append(copy(DEFAULT_WISH.dict()))
    assert "id" in RESP.json().pop()
    WISHES.clear()


def test_listing_wishes_return_one_wish_with_name():
    WISHES.append(copy(DEFAULT_WISH.dict()))
    assert "name" in RESP.json().pop()
    WISHES.clear()


def test_listing_wishes_return_one_wish_with_description():
    WISHES.append(copy(DEFAULT_WISH.dict()))
    assert "description" in RESP.json().pop()
    WISHES.clear()


def test_listing_wishes_return_one_wish_with_image_link():
    WISHES.append(copy(DEFAULT_WISH.dict()))
    assert "image_link" in RESP.json().pop()
    WISHES.clear()


def test_listing_wishes_return_one_wish_withlink():
    WISHES.append(copy(DEFAULT_WISH.dict()))
    assert "link" in RESP.json().pop()
    WISHES.clear()


def test_listing_wishes_return_one_wish_with_have():
    WISHES.append(copy(DEFAULT_WISH.dict()))
    assert "have" in RESP.json().pop()
    WISHES.clear()


def test_wishlist_should_accept_post():
    resp = TestClient(app).post("/wishlist")
    assert resp.status_code != 405


def test_created_wish_should_have_name():
    resp = TestClient(app).post("/wishlist", json={})
    assert resp.status_code == 422


def test_create_wish_endpoint_should_return_created_wish_itself():
    temp_wish = {"name": "cadeira 2",
                 "description": "",
                 "image_link": "",
                 "link": "",
                 "have": False
                 }

    client = TestClient(app)
    resp = client.post("/wishlist", json=temp_wish)
    resp_json = resp.json()
    resp_json.pop("id")
    assert resp_json == temp_wish
    WISHES.clear()


def test_creating_wish_should_return_201():
    temp_wish = {"name": "cadeira 2",
                 "description": "",
                 "image_link": "",
                 "link": "",
                 "have": False
                 }

    client = TestClient(app)
    resp = client.post("/wishlist", json=temp_wish)
    assert resp.status_code == 201
    WISHES.clear()


def test_creating_wishes_should_return_unique_id():
    temp_wish1 = {"name": "cadeira 2",
                  "description": "",
                  "image_link": "",
                  "link": "",
                  "have": False
                  }
    client = TestClient(app)
    resp1 = client.post("/wishlist", json=temp_wish1)

    temp_wish2 = {"name": "cadeira 2",
                  "description": "",
                  "image_link": "",
                  "link": "",
                  "have": False
                  }

    client = TestClient(app)
    resp2 = client.post("/wishlist", json=temp_wish2)

    assert resp1.json()["id"] != resp2.json()["id"]
    WISHES.clear()


def test_searching_for_invalid_id_should_return_404():
    client = TestClient(app)
    resp = client.get("/wishlist/-1")
    assert resp.status_code == 404


def test_serching_for_valid_id_should_return_200():
    WISHES.append(copy(DEFAULT_WISH.dict()))
    client = TestClient(app)
    resp = client.get("/wishlist/2")
    assert resp.status_code == 200
    WISHES.clear()


def test_deleting_wish_with_invalid_id_should_return_404():
    client = TestClient(app)
    resp = client.delete("/wishlist/-1")
    assert resp.status_code == 404


def test_deleting_wish_with_valid_id_should_return_404():
    WISHES.append(copy(DEFAULT_WISH.dict()))
    client = TestClient(app)
    resp = client.delete("/wishlist/1")
    assert resp.status_code == 404
    WISHES.clear()


def test_deleting_wish_removes_from_wishlist():
    WISHES.append(copy(DEFAULT_WISH.dict()))
    client = TestClient(app)
    client.delete("/wishlist/1")
    resp = client.get("/wishlist/1")
    assert resp.status_code == 404
    WISHES.clear()


def test_creating_task_should_add_to_tasks_list():
    temp_wish = {"name": "cadeira",
                 "description": "",
                 "image_link": "",
                 "link": "",
                 "have": False
                 }
    client = TestClient(app)
    client.post("/wishlist", json=temp_wish)
    assert len(WISHES) != 0
    WISHES.clear()


WISHES.clear()
