"""Module to extract free proxies from various free proxy listings"""

import asyncio
from .scraper import _extract_proxies_free_proxy_list_net
from .requester import make_request

def extract_proxy(https=False, proxy_count=300):
    """Function to extract proxies"""
    if proxy_count > 300:
        return {"error" : "current maximum allowed values is 300"}
    html_response = asyncio.run(make_request("https://free-proxy-list.net/"))
    if isinstance(html_response, dict):
        return html_response
    else:
        return _extract_proxies_free_proxy_list_net(html_response, https, proxy_count)
