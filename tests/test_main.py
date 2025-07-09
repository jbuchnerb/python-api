import sys
import os


# Agrega la carpeta raíz del proyecto al sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hola, mundo"}


def test_saludo():
    response = client.get("/saludo/Johann")
    assert response.status_code == 200
    assert response.json() == {"saludo": "Hola, Johann!"}
