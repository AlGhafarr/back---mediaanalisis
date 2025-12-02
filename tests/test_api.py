import pytest
from fastapi.testclient import TestClient
from app.main import app


@pytest.fixture
def client():
    return TestClient(app)


def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_list_servers(client):
    response = client.get("/api/v1/infrastructure/servers")
    assert response.status_code == 200
    assert "servers" in response.json()


def test_list_domains(client):
    response = client.get("/api/v1/infrastructure/domains")
    assert response.status_code == 200
    assert "domains" in response.json()


def test_list_networks(client):
    response = client.get("/api/v1/infrastructure/networks")
    assert response.status_code == 200
    assert "networks" in response.json()


def test_list_websites(client):
    response = client.get("/api/v1/infrastructure/websites")
    assert response.status_code == 200
    assert "websites" in response.json()
