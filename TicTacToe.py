from setup import set_playing_mode, exit_or_play_again
from game import Game


def main():
    mode, first_player, second_player, user_name, other_name = set_playing_mode()

    game = Game(mode, first_player, second_player, user_name, other_name)

    game.play_game()
    while exit_or_play_again() == 1:
        game.restart_game()
    main()


main()
