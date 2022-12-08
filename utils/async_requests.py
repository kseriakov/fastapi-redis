import aiohttp


async def async_get_request(path: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(path) as response:
            return await response.json()
