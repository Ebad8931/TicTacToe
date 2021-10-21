class Game:

    def __init__(self, mode, first_player, second_player, user_name, other_name):
        self.playing_mode = mode
        self.playerX = first_player  # PlayerX will always be user
        self.playerO = second_player  # Will be assigned after selection of Mode
        self.playerX_name = user_name
        self.playerO_name = other_name

        self.game_ended = False
        self.winner = '-'
        self.current_player = self.playerX  # default starting player

        self.board = ['-', '-', '-',
                      '-', '-', '-',
                      '-', '-', '-']
        self.possible_moves = list(range(9))

    def print_board(self):
        print(self.board[0], self.board[1], self.board[2])
        print(self.board[3], self.board[4], self.board[5])
        print(self.board[6], self.board[7], self.board[8])

    def switch_player(self):
        if self.current_player == self.playerX:
            self.current_player = self.playerO
        elif self.current_player == self.playerO:
            self.current_player = self.playerX

    def execute_move(self, move):
        if self.current_player == self.playerX:
            self.board[move] = 'X'
        elif self.current_player == self.playerO:
            self.board[move] = 'O'
        self.possible_moves.remove(move)

    def get_move(self):
        from setup import PlayerType
        # This function returns any value between 0 and 8
        if self.current_player == PlayerType.user.value or self.current_player == PlayerType.otherUser.value:
            return self.get_user_move()
        elif self.current_player == PlayerType.easyAI.value:
            return self.get_easy_move()
        elif self.current_player == PlayerType.mediumAI.value:
            return self.get_medium_move()
        elif self.current_player == PlayerType.hardAI.value:
            return self.get_hard_move()

    def get_user_move(self):
        move = int(input('Select Location (0-8) : '))
        if move in self.possible_moves:
            return move
        else:
            print("Invalid Input!")
            return self.get_user_move()

    # AI functions
    def take_winning_move(self):
        move = None
        for x in self.possible_moves:
            if self.current_player == self.playerX:
                self.board[x] = 'X'
            elif self.current_player == self.playerO:
                self.board[x] = 'O'
            if self.winning_condition_met():
                self.board[x] = '-'
                move = x
                break
            self.board[x] = '-'
        return move

    def block_winning_move(self):
        move = None
        for x in self.possible_moves:
            if self.current_player == self.playerX:
                self.board[x] = 'O'
            elif self.current_player == self.playerO:
                self.board[x] = 'X'
            if self.winning_condition_met():
                self.board[x] = '-'
                move = x
                break
            self.board[x] = '-'
        return move

    def get_easy_move(self):
        from random import randint
        if len(self.possible_moves) <= 5:  # min moves before somebody can win = 4
            x = self.take_winning_move()
            if x is not None:
                return x
        if len(self.possible_moves) <= 6:  # min moves before opponent can win = 3
            x = self.block_winning_move()
            if x is not None:
                return x
        x = randint(0, len(self.possible_moves) - 1)
        return self.possible_moves[x]

    def get_medium_move(self):
        return self.get_easy_move()

    def get_hard_move(self):
        return self.get_easy_move()

    def is_draw(self):
        if '-' not in self.board:
            self.game_ended = True

    def winning_condition_met(self):
        if (self.board[0] == self.board[1] == self.board[2] != '-') \
                or (self.board[3] == self.board[4] == self.board[5] != '-') \
                or (self.board[6] == self.board[7] == self.board[8] != '-') \
                or (self.board[0] == self.board[3] == self.board[6] != '-') \
                or (self.board[1] == self.board[4] == self.board[7] != '-') \
                or (self.board[2] == self.board[5] == self.board[8] != '-') \
                or (self.board[0] == self.board[4] == self.board[8] != '-') \
                or (self.board[2] == self.board[4] == self.board[6] != '-'):
            return True
        else:
            return False

    def check_winner(self):
        if self.winning_condition_met():
            self.winner = self.current_player
            self.game_ended = True
        else:
            return

    def play_game(self):
        self.print_board()
        while not self.game_ended:
            self.execute_move(self.get_move())
            self.check_winner()
            self.is_draw()
            self.print_board()
            print('')
            self.switch_player()
        if self.winner == '-':
            print("Game is a Tie!")
        elif self.winner == self.playerX:
            print(self.playerX_name + ' Wins!')
        elif self.winner == self.playerO:
            print(self.playerO_name + ' Wins!')

    def restart_game(self):
        if not self.game_ended:
            print('Invalid request! Cannot reinitialize')
        if self.winner != '-':
            self.current_player = self.winner
            self.winner = '-'

        self.board = ['-', '-', '-',
                      '-', '-', '-',
                      '-', '-', '-']
        self.possible_moves = list(range(9))
        self.game_ended = False
        self.play_game()
