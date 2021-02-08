import pytest
import aiohttp

from src.client import AsyncTestApiClient
from src.models import Status, UpdateRequest, Permission
from tests.functional.testdata.update_user import OK_RESPONSE, ERROR_RESPONSE, REQUEST


@pytest.mark.asyncio
async def test_update_user_ok(mock_server):
    server = mock_server(
        url='/user/2/update',
        method='post',
        request=REQUEST,
        response=OK_RESPONSE,
    )

    update_request = UpdateRequest(
        active="1",
        blocked=True,
        name='Petr Petrovich',
        permissions=[
            Permission(id=1, permission="comment")
        ]
    )

    async with server:
        async with AsyncTestApiClient(url=f'http://localhost:{server.port}') as client:
            resp = await client.update_user(user_id=2, token='dsfd79843r32d1d3dx23d32d', request=update_request)
        assert resp.status == Status.ok.value


@pytest.mark.asyncio
async def test_update_user_error(mock_server):
    server = mock_server(
        url='/user/2/update',
        method='post',
        request=REQUEST,
        response=ERROR_RESPONSE,
    )

    update_request = UpdateRequest(
        active="1",
        blocked=True,
        name='Petr Petrovich',
        permissions=[
            Permission(id=1, permission="comment")
        ]
    )

    async with server:
        async with AsyncTestApiClient(url=f'http://localhost:{server.port}') as client:
            resp = await client.update_user(user_id=2, token='dsfd79843r32d1d3dx23d32d', request=update_request)
        assert resp.status == Status.error.value
