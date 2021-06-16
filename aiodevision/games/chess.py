from aiodevision.enums import *
from aiodevision.errors import *
from aiodevision.baseclasses import *
import typing

class Chess:
    def __init__(self, client):
        self.client = client
        self.token = client.token
        self.http = self.client.http
    
    async def start(self, data: typing.Union[ChessData, dict]) -> typing.Union[dict, typing.Any]:
        if not self.token:
            raise TokenRequired('A Token is required to access this endpoint')

        if not isinstance(data, (ChessData, dict)):
            raise InvalidData(f'Expected ChessData or dict but got {data.__class__.__name__} instead')

        payload = {}

        if isinstance(data, ChessData):
            payload = data.to_payload()
        elif isinstance(data, dict):
            payload = data

        if 'white-theme' not in payload:
            raise InvalidData("Missing 'white-theme' key.")
        if 'black-theme' not in payload:
            raise InvalidData("Missing 'black-theme' key.")
        if 'board-theme' not in payload:
            raise InvalidData("Missing 'board-theme' key.")

        return await self.client.http.request('POST', '/api/games/chess', data=payload) as resp:

    async def chess_render(self, data: typing.Union[ChessRender, dict], arrow: typing.Union[typing.Any, None] = None):
        if not self.token:
            raise TokenRequired('A Token is required to access this endpoint')

        if not isinstance(data, (ChessRender, dict)):
            raise InvalidData(f'Expected ChessRender or dict but got {data.__class__.__name__} instead')

        payload = {}

        if isinstance(data, ChessRender):
            payload = data.to_payload()
        elif isinstance(data, dict):
            payload = data

        return await self.client.http.request('POST', '/api/games/chess/render', data=payload)

    async def chess_turn(self, data: typing.Union[ChessTurn, dict]):
        if not self.token:
            raise TokenRequired('A Token is required to access this endpoint')

        if not isinstance(data, (ChessTurn, dict)):
            raise InvalidData(f'Expected ChessTurn or dict but got {data.__class__.__name__} instead')

        payload = {}

        if isinstance(data, ChessTurn):
            payload = data.to_payload()
        elif isinstance(data, dict):
            payload = data

        return await self.client.http.request('POST', '/api/games/chess/turn', data=payload)

    async def chess_transcript(self, data: typing.Union[ChessTranscript, dict]):
        if not self.token:
            raise TokenRequired('A Token is required to access this endpoint')

        if not isinstance(data, (ChessTranscript, dict)):
            raise InvalidData(f'Expected ChessTranscript or dict but got {data.__class__.__name__} instead')

        payload = {}

        if isinstance(data, ChessTranscript):
            payload = data.to_payload()
        elif isinstance(data, dict):
            payload = data

        resp = await self.client.http.request('POST', '/api/games/chess', data=payload, raw=True)
        return await resp.text()
