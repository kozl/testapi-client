import asyncio

from src.client import AsyncTestApiClient
from src.models import Status


async def main():
    async with AsyncTestApiClient(url='http://testapi.ru') as client:
        auth = await client.authorize(login="kozl", password="qwertyuiop")
        if auth.status != Status.ok.value:
            print(f'Can\'t authorize, got {auth.status} status')
            return

        user_info = await client.get_user("hotmaps", auth.token)
        if user_info.status != Status.ok.value:
            print(f'Can\'t get user, got {user_info.status} status')
            return

        user_info.blocked = False
        update_status = await client.update_user(
            user_id=user_info.id,
            token=auth.token,
        )
        if update_status.status != Status.ok.value:
            print(f'Can\'t update user, got {update_status.status} status')
            return
        print("Whooray! 🎉")

if __file__ == '__main__':
    asyncio.run(main())
