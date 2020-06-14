from enum import Enum


# Game Initial Setup
class Mode(Enum):
    singlePlayer = 1
    twoPlayer = 2
    exit = 3


class PlayerType(Enum):
    user = 1
    otherUser = 2
    easyAI = 3
    mediumAI = 4
    hardAI = 5
