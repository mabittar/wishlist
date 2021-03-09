from starlette.testclient import TestClient
from app.server.app import app

client = TestClient(app)


def test_main_status_code():
    response = client.get("/")
    assert response.status_code == 200


def test_main_status_code():
    response = client.get("/wishlist")
    assert len(response.json()) == 2


def test_quando_lista_desejos_retorno_deve_ser_json():
    cliente = TestClient(app)
    response = cliente.get("/wishlist")
    assert response.headers["Content-Type"] == "application/json"


def test_quando_listar_desejos_retorno_deve_ser_um_dicionario():
    cliente = TestClient(app)
    response = cliente.get("/tarefas")
    assert isinstance(response.json(), dict)
