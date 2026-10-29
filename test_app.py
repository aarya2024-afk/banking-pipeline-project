import pytest
from app import app, ACCOUNT_DATA

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_check_balance(client):
    ACCOUNT_DATA["balance"] = 100
    response = client.get("/")
    assert response.status_code == 200
    assert b"Current Balance: $100" in response.data

def test_deposit(client):
    ACCOUNT_DATA["balance"] = 100
    response = client.post("/deposit", data={"amount": "50"})
    assert response.status_code == 302
    assert ACCOUNT_DATA["balance"] == 150
