import enum

class Enum(enum.Enum):
    def __str__(self):
        return self.name

class ChessPiece(Enum):
    white = 0
    black = 1

class ChessPieceTheme(Enum):
    eight_bit = 0
    glass = 1
    bases = 2
    classic = 3
    game_room = 4
    graffiti = 5
    lolz = 6
    neo = 7
    neo_wood = 8
    ocean = 9
    wood = 10
    
class BoardTheme(Enum):
    eight_bit = 0
    glass = 1
    graffiti = 2
    green = 3
    lolz = 4
    neon = 5
    overlay = 6
    parchment = 7
    walnut = 8
