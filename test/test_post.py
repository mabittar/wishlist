from app.schemas import WISHES, Wish, fake_wish_db
from starlette.testclient import TestClient
from copy import copy
from app.main import app

DEFAULT_WISH = Wish(id=1, name="mouse", description="mouse sem fio",
                    image_link="https://www.corsair.com/corsairmedia/sys_master/productcontent/ch-9315311-na-dark_core_rgb_se_04.png",
                    link="https://www.corsair.com/br/pt/Categorias/Produtos/Mouses-gamer/Wireless-Gaming-Mice/DARK-CORE-RGB-PRO-SE-Wireless-Gaming-Mouse/p/CH-9315511-NA",
                    have=False)

TEMP_WISH = {"name": "cadeira 2", "description": "", "image_link": "", "link": "", "have": False
             }


def test_wishlist_should_accept_post():
    resp = TestClient(app).post("/wishlist")
    assert resp.status_code != 405


def test_created_wish_should_have_name():
    resp = TestClient(app).post("/wishlist", json={})
    assert resp.status_code == 422


def test_creating_wish_should_return_201():
    client = TestClient(app)
    resp = client.post("/wishlist", json=TEMP_WISH)
    assert resp.status_code == 201
    WISHES.clear()


def test_creating_wishes_should_return_unique_id():
    client = TestClient(app)
    resp1 = client.post("/wishlist", json=TEMP_WISH)

    temp_wish2 = {"name": "cadeira 1",
                  "description": "",
                  "image_link": "",
                  "link": "",
                  "have": False
                  }

    client = TestClient(app)
    resp2 = client.post("/wishlist", json=temp_wish2)

    assert resp1.json()["id"] != resp2.json()["id"]
    WISHES.clear()


def test_create_wish_endpoint_should_return_created_wish_itself():
    client = TestClient(app)
    resp = client.post("/wishlist", json=TEMP_WISH)
    resp_json = resp.json()
    resp_json.pop("id")
    assert resp_json == TEMP_WISH
    WISHES.clear()


# def test_creating_wish_should_add_to_wishlist():
#     client = TestClient(app)
#     client.post("/wishlist", json=TEMP_WISH)
#     assert len(WISHES) == 1
#     WISHES.clear()


WISHES.clear()
