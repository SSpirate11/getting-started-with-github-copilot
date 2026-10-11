from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)


def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    data = response.json()
    assert "Chess Club" in data


def test_signup_for_activity():
    response = client.post("/activities/Chess Club/signup?email=new_student@mergington.edu")
    assert response.status_code == 200
    assert "Signed up" in response.json()["message"]


def test_prevent_duplicate_signup():
    response = client.post("/activities/Chess Club/signup?email=michael@mergington.edu")
    assert response.status_code == 400
    assert "already signed up" in response.json()["detail"]
