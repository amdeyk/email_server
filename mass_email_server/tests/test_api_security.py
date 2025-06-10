import pytest
from fastapi import FastAPI, Depends
from fastapi.testclient import TestClient

from app.security.api_key import verify_api_key

app = FastAPI()

@app.get("/protected", dependencies=[Depends(verify_api_key)])
async def protected():
    return {"ok": True}

client = TestClient(app)


def test_protected_success():
    response = client.get("/protected", headers={"X-API-Key": "changeme"})
    assert response.status_code == 200
    assert response.json() == {"ok": True}


def test_protected_failure():
    response = client.get("/protected")
    assert response.status_code == 403
