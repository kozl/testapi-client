import pytest
import aiohttp

from src.client import AsyncTestApiClient
from src.models import Status
from tests.functional.testdata.auth import OK_RESPONSE, ERROR_RESPONSE


@pytest.mark.asyncio
async def test_auth_ok(mock_server):
    server = mock_server('/auth', OK_RESPONSE)
    async with server:
        async with AsyncTestApiClient(url=f'http://localhost:{server.port}') as client:
            resp = await client.authorize(login='test', password='12345')
        assert resp.token == 'dsfd79843r32d1d3dx23d32d'


@pytest.mark.asyncio
async def test_auth_error(mock_server):
    server = mock_server('/auth', ERROR_RESPONSE)
    async with server:
        async with AsyncTestApiClient(url=f'http://localhost:{server.port}') as client:
            resp = await client.authorize(login='test', password='12345')
        assert resp.status == Status.error.value
