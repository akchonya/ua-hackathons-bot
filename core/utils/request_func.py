import aiohttp


async def make_async_request(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()
