from asyncio import sleep
import aiohttp
from .errors import *

class HTTPClient:
    def __init__(self, client):
        self.client = client
        self.session = client.session
        self.headers = client.headers
        self.retry = client.retry
        self.base_url = client.base_url
        
    async def request(self, method: str, url: str, **kwargs):
        if not self.base_url.endswith("/"):
            self.base_url = (self.base_url + "/")
            self.client.base_url = (self.client.base_url + "/")
            
        base_url = self.base_url
            
        if not url.startswith(base_url):
            url = (base_url + url)
            
        headers = kwargs.pop("headers", None)
        session = kwargs.pop("session", self.session)
        retry = kwargs.pop("retry", self.retry)
        
        for _ in range(retry):
            async with cs.request(
                method, url, **kwargs
            ) as response:
                if response.status in [200, 201]:
                    try:
                        return await response.json()
                    except:
                        return response
                elif response.status in [400, 500]:
                    raise InternalServerError(response.reason)
                elif response.status == 403:
                    raise Banned()
                elif response.status == 429:
                    wait = float(response.headers["ratelimit-retry-after"])
                    await asyncio.sleep(wait)
                    continue
                elif response.status == 401:
                    raise TokenRequired(response.reason)
                elif response.status == 404:
                    if method == "DELETE":
                        return response
                    raise NotFound()
                elif response.status == 204:
                    return True

        raise MaxRetryReached(self.retry)
