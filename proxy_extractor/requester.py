import aiohttp
from .useragents import rand_user_agent

async def make_request(url):
    user_agent = rand_user_agent()
    headers = {
        "User-Agent": user_agent
    }

    async with aiohttp.ClientSession(headers=headers) as session:
        try:
            async with session.get(url) as resp:
                if resp.status == 200:
                    return await resp.text()
                else:
                    return {"error" : "server down"}
        except:
            return {"error" : "failed to retrieve url"}
    return {"error" : "request finished with none"}