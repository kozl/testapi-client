import aiohttp

from src.abstract import TestApiClient
from src.models import(
    UserInfoResponse,
    AuthResponse,
    UpdateResponse,
    UpdateRequest
)


class AsyncTestApiClient(TestApiClient):
    def __init__(self, url: str = "http://testapi.ru"):
        self.session = aiohttp.ClientSession()
        self.url = url

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.session.close()

    async def authorize(self, login, password: str) -> AuthResponse:
        params = {'login': login, 'pass': password}
        async with self.session.get(f'{self.url}/auth', params=params) as resp:
            return AuthResponse.parse_raw(await resp.text())

    async def get_user(self, username, token: str) -> UserInfoResponse:
        params = {'token': token}
        async with self.session.get(f'{self.url}/get-user/{username}', params=params) as resp:
            return UserInfoResponse.parse_raw(await resp.text())

    async def update_user(self, user_id: int, token: str, request: UpdateRequest) -> UpdateResponse:
        params = {'token': token}
        async with self.session.post(f'{self.url}/user/{user_id}/update', params=params, json=request.dict()) as resp:
            return UpdateResponse.parse_raw(await resp.text())
