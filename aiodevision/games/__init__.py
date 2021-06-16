import aiodevision
from .chess import Chess

class Game:
    def __init__(self, client):
        self.client = client
        
    @property
    async def chess(self):
        return Chess(self.client)
