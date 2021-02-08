import json
from typing import Optional

import pytest
import aiohttp


@pytest.fixture
async def mock_server():
    def inner(url, response: object, method: str = 'get', request: Optional[object] = None):
        app = aiohttp.web.Application()

        async def hander(req):
            resp = aiohttp.web.Response(text=json.dumps(response))
            if request:
                body = await req.text()
                if body != json.dumps(request):
                    resp = aiohttp.web.Response(status=404)
            return resp

        app.router.add_route(method, url, hander)
        server = aiohttp.test_utils.TestServer(app)

        return server
    return inner
