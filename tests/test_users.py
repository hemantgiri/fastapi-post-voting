from app import schemas
from app.config import settings
import pytest
from .database import client, session
from jose import jwt

def test_create_user(client):
    res = client.post("/users", json={"email" : "test@example.com", "password" : "123456"})
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "test@example.com"
    assert res.status_code == 201

def test_login_user(client, test_user):
    res = client.post("/login", data={"username" : test_user['email'], "password" : test_user['password']})
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.access_token, settings.secret_key, algorithms = [settings.algorithm])
    id = payload.get("user_id")
    assert id == test_user["id"]
    assert res.status_code == 200   

@pytest.mark.parametrize("email, password, status_code", [
     ('wrongemail@gmail.com', 'password123', 403),
    ('test@example.com', 'wrongpassword', 403),
    ('wrongemail@gmail.com', 'wrongpassword', 403),
    (None, 'password123', 422),
    ('test@example.com', None, 422)
])
def test_incorrect_login(client, test_user, email, password, status_code):
    res = client.post("/login", data={"username" : email, "password" : password})  
    assert res.status_code == status_code

