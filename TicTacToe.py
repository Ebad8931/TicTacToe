from enum import Enum

board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']


class PlayerType(Enum):
    user = 1
    easyAI = 2
    mediumAI = 3
    hardAI = 4


playerX = PlayerType.user.value     # PlayerX will always be user
playerO = 0                         # Will be assigned after selection of Mode
playerX_name = 'Not Assigned'
playerO_name = 'Not Assigned'


class Mode(Enum):
    singlePlayer = 1
    twoPlayer = 2


playing_mode = 0

current_player = playerX            # default starting player

GameEnded = False
Winner = '-'


def print_board():
    print(board[0], board[1], board[2])
    print(board[3], board[4], board[5])
    print(board[6], board[7], board[8])


def set_playing_mode():
    for x in Mode:
        print('Select ' + str(x.value) + ' for ' + x.name)
    mode = int(input())
    while mode <= 0 or mode > 2:
        print('Invalid choice. Select Again')
        mode = int(input())
    global playing_mode
    playing_mode = mode
    set_2nd_player()
    set_players_name()


def set_2nd_player():
    global playerO
    if playing_mode == Mode.singlePlayer.value:
        print('\nSelect 1 for Easy:')
        print('Select 2 for Medium:')
        print('Select 3 for Hard:')
        difficulty = int(input())
        while difficulty <= 0 or difficulty > 3:
            print('Invalid choice. Select Again')
            difficulty = int(input())
        if difficulty == 1:
            playerO = PlayerType.easyAI.value
        if difficulty == 2:
            playerO = PlayerType.mediumAI.value
        if difficulty == 3:
            playerO = PlayerType.hardAI.value
    if playing_mode == Mode.twoPlayer.value:
        playerO = PlayerType.user.value


def set_players_name():
    global playerX_name, playerO_name
    playerX_name = input("Enter Player 1's name: ")
    if playerO == PlayerType.user.value:
        playerO_name = input("Enter Player 2's name: ")
    elif playerO_name == PlayerType.easyAI.value or PlayerType.mediumAI.value or PlayerType.hardAI.value:
        playerO_name = 'Computer'


def switch_player(p):
    if p == playerX:
        return playerO
    if p == playerO:
        return playerX


def player_turn(p):
    x = input("Select Location (0-8) : ")
    x = int(x)
    if 0 <= x < 9 and board[x] == "-":
        board[x] = p
    else:
        print("Invalid Input!")
        player_turn(p)
    return


def is_draw():
    global GameEnded
    if '-' not in board:
        GameEnded = True


def check_winner():
    global Winner
    # check rows
    if board[0] == board[1] == board[2] != '-':
        Winner = board[0]
    elif board[3] == board[4] == board[5] != '-':
        Winner = board[3]
    elif board[6] == board[7] == board[8] != '-':
        Winner = board[6]
    # check columns
    elif board[0] == board[3] == board[6] != '-':
        Winner = board[0]
    elif board[1] == board[4] == board[7] != '-':
        Winner = board[1]
    elif board[2] == board[5] == board[8] != '-':
        Winner = board[2]
    # check diagonals
    elif board[0] == board[4] == board[8] != '-':
        Winner = board[0]
    elif board[2] == board[4] == board[6] != '-':
        Winner = board[2]
    else:
        return
    global GameEnded
    GameEnded = True


def two_payer_game():
    print_board()
    player = 'X'
    while not GameEnded:
        player_turn(player)
        check_winner()
        is_draw()
        print_board()
        player = switch_player(player)
    if Winner == '-':
        print("\nGame is a Tie!")
    else:
        print('\n' + Winner + ' WON!')


print(playing_mode)
set_playing_mode()
print(playing_mode)
print(playerX)
print(playerX_name)
print(playerO)
print(playerO_name)
