import typing

import msgspec
from starlette.requests import Request


class MSGSpecJSONRequest(Request):
    """
    Request using the high-performance msgspec library to parse JSON data.
    """

    async def json(self) -> typing.Any:
        if not hasattr(self, "_json"):
            body = await self.body()
            # noinspection PyAttributeOutsideInit
            self._json = msgspec.json.decode(body)
        return self._json
