'''
* TicTacToe Game
* TicTacToe Class
* CS043 - Final Project
* by Kian F.
'''

import random
from player import Player


class TicTacToe:

    def __init__(self):
        # show welcome message
        print()
        print('Welcome to Tic Tac Toe!')

        # prepare board
        self.board = []
        self.resetBoard()

        # create player objects
        player1 = Player(1, 'X')
        player2 = Player(2, 'O')
        self.players = [player1, player2]
        print('{} plays {}'.format(self.players[0].name, self.players[0].marker))
        print('{} plays {}'.format(self.players[1].name, self.players[1].marker))

        # randomly chose first player
        self.nextPlayer = random.randint(0, 1)
        print("{} starts first\n".format(self.players[self.nextPlayer].name))

    def __repr__(self):
        return "<TicTacToe By Kian F.>"

    def resetBoard(self):
        # this function fills the board list with spaces
        self.board = [' '] * 10

    def playNext(self):
        # this function draws the board and asks for next player's move, then checks for win or tie
        # it also returns true, if game can continue, otherwise returns false
        player = self.players[self.nextPlayer]

        self.__drawBoard()
        move = self.__getPlayerMove()

        # make move
        self.board[move] = player.marker

        # check for winner
        if self.__isWinner(player.marker):
            player.increaseScore()
            self.__drawBoard()
            print('Hooray! The winner is {}!!'.format(player.name))
            self.__showScores()
            print()
            return False
        else:
            if self.__isBoardFull():
                self.__drawBoard()
                print('The game is a tie!')
                self.__showScores()
                return False
            else:
                # switch to next player
                self.nextPlayer = 1 if self.nextPlayer == 0 else 0
                return True

    def __drawBoard(self):
        # This function prints out the board.
        # "board" is a list of 10 strings representing the board (ignore index 0)
        print()
        print('   |   |')
        self.__drawRow(7)
        print('   |   |')
        print('-----------')
        print('   |   |')
        self.__drawRow(4)
        print('   |   |')
        print('-----------')
        print('   |   |')
        self.__drawRow(1)
        print('   |   |')

    def __drawRow(self, start):
        # draws one row of board
        print(' ', end='')
        self.__mark(start)
        print(' | ', end='')
        self.__mark(start + 1)
        print(' | ', end='')
        self.__mark(start + 2)
        print()

    def __mark(self, position):
        # displays a symbol in the board. If the position is not filled, it shows position number
        letter = self.board[position]
        print(letter, end='')

    def __getPlayerMove(self):
        # Let the player type in his move.
        move = ' '
        player = self.players[self.nextPlayer]
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not self.board[int(move)] == ' ':
            print(' {} '.format(player.name), end='')
            move = input(' what is your next move? (1-9): ')
        return int(move)

    def __isWinner(self, le):
        # this function returns True if that player has won.
        bo = self.board
        return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # across the top
                (bo[4] == le and bo[5] == le and bo[6] == le) or  # across the middle
                (bo[1] == le and bo[2] == le and bo[3] == le) or  # across the bottom
                (bo[7] == le and bo[4] == le and bo[1] == le) or  # down the left side
                (bo[8] == le and bo[5] == le and bo[2] == le) or  # down the middle
                (bo[9] == le and bo[6] == le and bo[3] == le) or  # down the right side
                (bo[7] == le and bo[5] == le and bo[3] == le) or  # diagonal
                (bo[9] == le and bo[5] == le and bo[1] == le))  # diagonal

    def __isBoardFull(self):
        # Return True if every space on the board has been taken. Otherwise return False.
        for i in range(1, 10):
            if self.board[i] == ' ':
                return False
        return True

    def __showScores(self):
        # this functions shows 2 players' scores
        print('Scores:')
        for player in self.players:
            print("{}'s score: {}".format(player.name, player.score))
        print()



