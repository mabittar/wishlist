from app.schemas import WISHES, Wish, fake_wish_db
from starlette.testclient import TestClient
from copy import copy
from app.main import app

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


WISHES.clear()
