from typing import Any

import msgspec
from fastapi.responses import JSONResponse


class MsgSpecJSONResponse(JSONResponse):
    """
    JSON response using the high-performance msgspec library to serialize data to JSON.

    Read more about it in the
    [FastAPI docs for Custom Response - HTML, Stream, File, others](https://fastapi.tiangolo.com/advanced/custom-response/).
    """

    def render(self, content: Any) -> bytes:
        assert msgspec is not None, "msgspec must be installed to use MSGSPECResponse"
        return msgspec.json.encode(content)
