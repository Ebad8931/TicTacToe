board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']
GameEnded = False
Winner = '-'


def print_board():
    print(board[0], board[1], board[2])
    print(board[3], board[4], board[5])
    print(board[6], board[7], board[8])


def switch_player(p):
    if p == 'X':
        return 'O'
    elif p == 'O':
        return 'X'
    else:
        return 'Invalid'


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


print_board()
player = 'X'
while not GameEnded:
    player_turn(player)
    check_winner()
    print_board()
    player = switch_player(player)
if Winner == '-':
    print("Game is a Tie!")
else:
    print('\n' + Winner + ' WON!')
