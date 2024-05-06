from fastapi import FastAPI
from starlette.requests import Request
from starlette.testclient import TestClient

from fastapi_msgspec.responses import MsgSpecJSONResponse
from fastapi_msgspec.routing import MsgSpecRoute

app = FastAPI(default_response_class=MsgSpecJSONResponse)
app.router.route_class = MsgSpecRoute


@app.get("/")
def get_root():
    return {"msg": "Hello World", 1: 1}


@app.post("/")
def post_root(request: Request, item: dict):
    return item


client = TestClient(app)


def test_msgspec_route_class():
    with client:
        response = client.get("/")
    assert response.json() == {"msg": "Hello World", "1": 1}
    with client:
        response = client.post("/", json={"msg": "Hello World", 1: 1})
    assert response.json() == {"msg": "Hello World", "1": 1}
