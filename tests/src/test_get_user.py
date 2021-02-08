import pytest
import aiohttp

from src.client import AsyncTestApiClient
from src.models import Status
from tests.functional.testdata.get_user import OK_RESPONSE, NOT_FOUND_RESPONSE, ERROR_RESPONSE


@pytest.mark.asyncio
async def test_get_user_ok(mock_server):
    server = mock_server('/get-user/ivanov', OK_RESPONSE)
    async with server:
        async with AsyncTestApiClient(url=f'http://localhost:{server.port}') as client:
            resp = await client.get_user(username='ivanov', token='dsfd79843r32d1d3dx23d32d')
        assert resp.name == 'Ivanov Ivan'
        assert len(resp.permissions) == 3


@pytest.mark.asyncio
async def test_get_user_error(mock_server):
    server = mock_server('/get-user/ivanov', NOT_FOUND_RESPONSE)
    async with server:
        async with AsyncTestApiClient(url=f'http://localhost:{server.port}') as client:
            resp = await client.get_user(username='ivanov', token='dsfd79843r32d1d3dx23d32d')
        assert resp.status == Status.not_found.value


@pytest.mark.asyncio
async def test_get_user_error(mock_server):
    server = mock_server('/get-user/ivanov', ERROR_RESPONSE)
    async with server:
        async with AsyncTestApiClient(url=f'http://localhost:{server.port}') as client:
            resp = await client.get_user(username='ivanov', token='dsfd79843r32d1d3dx23d32d')
        assert resp.status == Status.error.value
