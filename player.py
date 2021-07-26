'''
* TicTacToe Game
* Player CLass
* CS043 - Final Project
* by Kian F.
'''


class Player:
    def __init__(self, number, marker):
        self.marker = marker  # X/O
        self.score = 0
        self.number = number
        self.name = ''
        self.__askPlayerName()

    def __repr__(self):
        return "<Player name={}, marker={}, score={}>".format(self.name, self.marker, self.score)

    def __askPlayerName(self):
        # this function asks for player's name
        while self.name == '':
            self.name = input("Enter Player {}'s Name:".format(self.number))

    def increaseScore(self):
        # this function increases the players score by 1
        self.score += 1



