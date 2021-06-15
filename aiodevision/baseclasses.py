from .enums import *
import typing

class ChessData:
    r"""
    The chess payload. This contains the board theme and the black and white chess piece theme.

    Paramaters
    ----------
    black: :class:`ChessPieceTheme`
        The theme for the black chess piece.
    white: :class:`ChessPieceTheme`
        The theme for the white chess piece.
    board: :class:`BoardTheme`
        The theme for the board.
    """
    def __init__(self, black: ChessPieceTheme, white: ChessPieceTheme, board: BoardTheme):
        self.black = black
        self.white = white
        self.board = board

    def to_payload(self):
        return {
            "white-theme": str(self.white),
            "black-theme": str(self.black),
            "board-theme": str(self.board)
        }

class ChessRender:
    r"""
    The chess payload for rendering. This contains the arrow and the board.

    Paramaters
    ----------
    board: :class:`dict`
        The board returned in chess endpoint.
    arrow: Any
        The arrows to be shown in the image.
    """
    def __init__(self, board: dict, arrow: typing.Any):
        self.board = board
        self.arrow = arrow

    def to_payload(self):
        return {
            "board": self.board,
            "arrow": self.arrow
        }

class ChessTurn:
    r"""
    The chess payload for turn endpoint.

    Paramaters
    ----------
    board: :class:`dict`
        The board returned in chess endpoint.
    turn: :class:`str`
        The turn of the chess. For example, 'a2-a4'
    player: :class:`ChessPiece`
        The player that is turning.
    """
    def __init__(self, board: dict, turn: str, player: ChessPiece):
        self.board = board
        self.turn = turn
        self.player = player

    def to_payload(self):
        return {
            "board": self.board,
            "turn": self.turn,
            "move-turn": str(self.player)
        }

class ChessTranscript:
    r"""
    The chess transcript.

    Paramaters
    ----------
    board: :class:`dict`
        The board returned in chess endpoint.
    """
    def __init__(self, board: dict):
        self.board = board

    def to_payload(self):
        return {
            "board": self.board
        }
