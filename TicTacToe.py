from enum import Enum
from random import randint


class Mode(Enum):
    singlePlayer = 1
    twoPlayer = 2
    EXIT = 3


class PlayerType(Enum):
    user = 1
    otherUser = 2
    easyAI = 3
    mediumAI = 4
    hardAI = 5


playing_mode = 0
playerX = PlayerType.user.value     # PlayerX will always be user
playerO = 0                         # Will be assigned after selection of Mode
playerX_name = 'Not Assigned'
playerO_name = 'Not Assigned'

board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']
possible_moves = list(range(9))
GameEnded = False
Winner = '-'
current_player = playerX            # default starting player


def reinitialize_game():
    global board, possible_moves, GameEnded, Winner, current_player

    if not GameEnded:
        print('Invalid request! Cannot reinitialize')
    if Winner != '-':
        current_player = Winner
        Winner = '-'

    board = ['-', '-', '-',
             '-', '-', '-',
             '-', '-', '-']
    possible_moves = list(range(9))
    GameEnded = False


def print_board():
    print(board[0], board[1], board[2])
    print(board[3], board[4], board[5])
    print(board[6], board[7], board[8])


def set_playing_mode():
    global playing_mode
    for x in Mode:
        print('Select ' + str(x.value) + ' for ' + x.name)
    playing_mode = int(input())
    while playing_mode <= 0 or playing_mode > 3:
        print('Invalid choice. Select Again')
        playing_mode = int(input())
    if playing_mode == Mode.EXIT.value:
        exit()
    set_2nd_player()
    set_players_name()


def set_2nd_player():
    global playerO
    if playing_mode == Mode.singlePlayer.value:
        print('Select 1 for Easy')
        print('Select 2 for Medium')
        print('Select 3 for Hard')
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
    if move in possible_moves:
        return move
    else:
        print("Invalid Input!")
        return get_user_move()


# AI functions
def take_winning_move():
    move = None
    for x in possible_moves:
        if current_player == playerX:
            board[x] = 'X'
        elif current_player == playerO:
            board[x] = 'O'
        if winning_condition_met():
            board[x] = '-'
            move = x
            break
        board[x] = '-'
    return move


def block_winning_move():
    move = None
    for x in possible_moves:
        if current_player == playerX:
            board[x] = 'O'
        elif current_player == playerO:
            board[x] = 'X'
        if winning_condition_met():
            board[x] = '-'
            move = x
            break
        board[x] = '-'
    return move


def get_easy_move():
    if len(possible_moves) <= 5:    # min moves before somebody can win = 4
        x = take_winning_move()
        if x is not None:
            return x
        x = block_winning_move()
        if x is not None:
            return x
    x = randint(0, len(possible_moves)-1)
    return possible_moves[x]


def get_medium_move():
    return get_easy_move()


def get_hard_move():
    return get_easy_move()


def execute_move(move):
    if current_player == playerX:
        board[move] = 'X'
    elif current_player == playerO:
        board[move] = 'O'
    possible_moves.remove(move)


def is_draw():
    global GameEnded
    if '-' not in board:
        GameEnded = True


def winning_condition_met():
    if (board[0] == board[1] == board[2] != '-') \
            or (board[3] == board[4] == board[5] != '-') \
            or (board[6] == board[7] == board[8] != '-') \
            or (board[0] == board[3] == board[6] != '-') \
            or (board[1] == board[4] == board[7] != '-') \
            or (board[2] == board[5] == board[8] != '-') \
            or (board[0] == board[4] == board[8] != '-') \
            or (board[2] == board[4] == board[6] != '-'):
        return True
    else:
        return False


def check_winner():
    global Winner, GameEnded
    if winning_condition_met():
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


def exit_or_play_again():
    print('Select 1 to Play Again')
    print('Select 2 to go back to Main Menu')
    choice = int(input())
    while choice <= 0 or choice > 2:
        print('Invalid choice. Select Again')
        choice = int(input())

    reinitialize_game()
    if choice == 2:
        global current_player
        current_player = playerX
        set_playing_mode()
    play_game()
    exit_or_play_again()


set_playing_mode()
play_game()
exit_or_play_again()
