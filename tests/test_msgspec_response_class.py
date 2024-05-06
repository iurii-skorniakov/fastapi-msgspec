from fastapi import FastAPI
from fastapi_msgspec.responses import MsgSpecJSONResponse
from starlette.testclient import TestClient

app = FastAPI(default_response_class=MsgSpecJSONResponse)


@app.get("/")
def get_root():
    return {"msg": "Hello World", 1: 1}


client = TestClient(app)


def test_msgspec_response_class():
    with client:
        response = client.get("/")
    assert response.json() == {"msg": "Hello World", "1": 1}
