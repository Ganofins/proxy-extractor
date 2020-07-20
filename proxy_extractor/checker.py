import aiohttp
from .useragents import rand_user_agent

async def proxy_check(proxy, timeout):
    """Funtion to check whether a proxy is working or not"""
    try:
        #would need to use http even for https proxy
        host_type = "http://"
        proxy_url = host_type + proxy["ip"] + ":" + proxy["port"]
        async with aiohttp.ClientSession() as session:
            async with session.get(host_type + "httpbin.org/ip", proxy=proxy_url, timeout=timeout) as response:
                if response.status == 200:
                    return True
                return False
    except:
        return False