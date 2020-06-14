from config import Mode, PlayerType

playing_mode = 0
playerX = PlayerType.user.value     # PlayerX will always be user
playerO = 0                         # Will be assigned after selection of Mode
playerX_name = 'Not Assigned'
playerO_name = 'Not Assigned'


def set_playing_mode():
    global playing_mode
    for x in Mode:
        print('Select ' + str(x.value) + ' for ' + x.name)
    playing_mode = int(input())
    while playing_mode <= 0 or playing_mode > 3:
        print('Invalid choice. Select Again')
        playing_mode = int(input())
    if playing_mode == Mode.exit.value:
        exit()
    set_2nd_player()
    set_players_name()
    return playing_mode, playerX, playerO, playerX_name, playerO_name


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


def exit_or_play_again():
    print('Select 1 to Play Again')
    print('Select 2 to go back to Main Menu')
    choice = int(input())
    while choice <= 0 or choice > 2:
        print('Invalid choice. Select Again')
        choice = int(input())
    return choice
