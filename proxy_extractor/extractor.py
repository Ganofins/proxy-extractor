"""Module to extract free proxies from various free proxy listings"""

import asyncio
from .scraper import _extract_proxies_free_proxy_list_net
from .requester import make_request
from .checker import proxy_check

working_proxy_list = []

class AsyncIter:    
    def __init__(self, items):    
        self.items = items

    async def __aiter__(self):    
        for item in self.items:    
            yield item


async def extract_proxies(https, proxy_count):
    """Function to extract proxies"""
    if proxy_count > 300:
        return {"error" : "current maximum allowed limit is 300"}
    html_response = await make_request("https://free-proxy-list.net/")
    if isinstance(html_response, dict):
        return html_response
    else:
        return _extract_proxies_free_proxy_list_net(html_response, https)


async def get_extracted_proxies(proxy_list):
    async for each_proxy in proxy_list:
        yield each_proxy


async def proxy_remove(proxy, proxy_count, timeout):
    """Function to remove not working proxy"""
    if await proxy_check(proxy, timeout):
        working_proxy_list.append(proxy)
    if len(working_proxy_list) == proxy_count:
        return True


tasks = []
async def create_jobs(proxy_list, https, proxy_count, timeout):
    async for each_proxy in get_extracted_proxies(proxy_list):
        task = asyncio.ensure_future(proxy_remove(each_proxy, proxy_count, timeout))
        tasks.append(task)


def extract_proxy(https=False, proxy_count=100, timeout=50):
    """Function to extract proxies"""
    if proxy_count == None:
        proxy_count = 100
    if timeout == None:
        timeout = 50
    proxy_list = asyncio.run(extract_proxies(https, proxy_count))
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    proxies = AsyncIter(proxy_list)
    loop.run_until_complete(create_jobs(proxies, https, proxy_count, timeout))
    loop.run_until_complete(asyncio.wait(tasks))
    return working_proxy_list