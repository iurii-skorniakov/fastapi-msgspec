# fastapi-msgspec

[msgspec](https://github.com/jcrist/msgspec) integration for [FastAPI](https://github.com/tiangolo/fastapi/)

## Installation
```shell
pip install fastapi-msgspec
```

## Usage
```python
from fastapi import FastAPI

from fastapi_msgspec.responses import MsgSpecJSONResponse
from fastapi_msgspec.routing import MsgSpecRoute

app = FastAPI(default_response_class=MsgSpecJSONResponse)
app.router.route_class = MsgSpecRoute

```