'''
* TicTacToe Game
* Main Module
* CS043 - Final Project
* by Kian F.
'''

from tictactoe import TicTacToe


def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


# create a TicTacToe object for the game
ttt = TicTacToe()

# main loop
while True:

    # game loop
    while True:
        # stop if no more move left
        if not ttt.playNext():
            break

    if not playAgain():
        print("Thank you for playing!")
        break

    # continue with playing a new game
    ttt.resetBoard()
