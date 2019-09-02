from enum import Enum

board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']


class PlayerType(Enum):
    user = 1
    otherUser = 2
    easyAI = 3
    mediumAI = 4
    hardAI = 5


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
        elif difficulty == 2:
            playerO = PlayerType.mediumAI.value
        elif difficulty == 3:
            playerO = PlayerType.hardAI.value
    elif playing_mode == Mode.twoPlayer.value:
        playerO = PlayerType.otherUser.value


def set_players_name():
    global playerX_name, playerO_name
    playerX_name = input("Enter Player 1's name: ")
    if playerO == PlayerType.user.value or playerO == PlayerType.otherUser.value:
        playerO_name = input("Enter Player 2's name: ")
    elif playerO == PlayerType.easyAI.value or playerO == PlayerType.mediumAI.value \
            or playerO == PlayerType.hardAI.value:
        playerO_name = 'Computer'


def switch_player():
    global current_player
    if current_player == playerX:
        current_player = playerO
    elif current_player == playerO:
        current_player = playerX


def get_move():
    # This function returns any value between 0 and 8
    if current_player == PlayerType.user.value or current_player == PlayerType.otherUser.value:
        return get_user_move()
    elif current_player == PlayerType.easyAI.value:
        return get_easy_move()
    elif current_player == PlayerType.mediumAI.value:
        return get_medium_move()
    elif current_player == PlayerType.hardAI.value:
        return get_hard_move()


def get_user_move():
    move = int(input('Select Location (0-8) : '))
    if 0 <= move < 9 and board[move] == "-":
        return move
    else:
        print("Invalid Input!")
        return get_user_move()


def get_easy_move():
    from random import randint
    x = 0
    while board[x] != '-':
        x = randint(0, 8)
    return x


def get_medium_move():
    from random import randint
    x = 0
    while board[x] != '-':
        x = randint(0, 8)
    return x


def get_hard_move():
    from random import randint
    x = 0
    while board[x] != '-':
        x = randint(0, 8)
    return x


def execute_move(move):
    if current_player == playerX:
        board[move] = 'X'
    elif current_player == playerO:
        board[move] = 'O'


def is_draw():
    global GameEnded
    if '-' not in board:
        GameEnded = True


def check_winner():
    global Winner, GameEnded
    # check rows
    if (board[0] == board[1] == board[2] != '-') \
            or (board[3] == board[4] == board[5] != '-') \
            or (board[6] == board[7] == board[8] != '-') \
            or (board[0] == board[3] == board[6] != '-') \
            or (board[1] == board[4] == board[7] != '-') \
            or (board[2] == board[5] == board[8] != '-') \
            or (board[0] == board[4] == board[8] != '-') \
            or (board[2] == board[4] == board[6] != '-'):
        Winner = current_player
        GameEnded = True
    else:
        return


def play_game():
    print_board()
    while not GameEnded:
        execute_move(get_move())
        check_winner()
        is_draw()
        print_board()
        switch_player()
    if Winner == '-':
        print("\nGame is a Tie!")
    elif Winner == playerX:
        print('\n' + playerX_name + ' Wins!')
    elif Winner == playerO:
        print('\n' + playerO_name + ' Wins!')


set_playing_mode()
play_game()
