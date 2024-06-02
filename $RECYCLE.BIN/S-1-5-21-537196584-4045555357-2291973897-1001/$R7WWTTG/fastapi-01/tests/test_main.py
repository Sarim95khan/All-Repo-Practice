from fastapi_01.main import app
from fastapi.testclient import TestClient

def test_root_path():
    client = TestClient(app = app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {'message': 'Hello Yahya'}