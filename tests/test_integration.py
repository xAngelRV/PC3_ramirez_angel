from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_sumar_integracion():
    response = client.get("/sumar?a=3&b=4")
    assert response.status_code == 200
    assert response.json() == {"resultado": 7}


def test_promedio_lista_valida():
    response = client.post("/promedio", json={"valores": [10.0, 20.0, 30.0]})
    assert response.status_code == 200
    assert response.json() == {"promedio": 20.0}


def test_promedio_lista_vacia():
    response = client.post("/promedio", json={"valores": []})
    assert response.status_code == 400
    assert response.json() == {"detail": "Lista vacía"}


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
