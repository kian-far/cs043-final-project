## CS043 Final Project 
# Tic-Tac-Toe 
By: Kian F.

## Requirements

Objective: Building an Object-Oriented program allowing 2 players to play the tic-tac-toe game on screen.

**About the game**
Tic-tac-toe is a 2-player game on a 3x3 game board, in which players take turns to occupy the spaces on the game board in such a way to complete a row, column, or a diagonal stright line to win.

To track which space belongs to which player, one player uses X and the other uses O. The first player is chosen by a random draw.

If a player can take a row, column, or a diagonal line of 3 spaces on the board, they win the game. If all the spaces on the board are taken without a winner, the game will be a tie.

The player's score increases by each win and at the end, the player with the highest score is the winner.


       |   |
     7 | 8 | 9
       |   |
    -----------
       |   |
     4 | 5 | 6
       |   |
    -----------
       |   |
     1 | 2 | 3
       |   |




## Design
This application consists of 3 files:
 - main.py: the main module
 - tictactoe.py: the TicTacToe class definition
 - player.py: the Player class definition

 **Player Class**
 This class represents a player for the game. The Player class has the following data attributes:

 - name
 - marker (X or O)
 - score
 - number (1 or 2) 
 
It also has the following methods:
 - __init __: initializes the data attributes and asks for the player's name
 - increaseScore: to increase player's score
 - __askPlayerName: to ask player's name

**TicTacToe Class**
This class has the main code manage the game steps and rules. The TicTacToe class, uses 2 objects of type Player class to manage players.
The data attributes of TicTacToe class are:

 - board: represents the game board spaces
 - players: a list of 2 Player objects
 - nextPlayer: value of 0 or 1 pointing to the next player in the "players" list
 
 The method attributes of this class are:
 

 - __init __: initializes the game board, creates players objects, and chooses the first player
 - resetBoard: resets the board list by filling it in with spaces
 - playNext: asks for player's move, updates the board and checks whether the outcome is a win or tie
 - __drawBoard: draws the current state of the board
 - __drawRow: draws one row of the board
 - __mark: color marks one space on the board based on value in the space
 - __getPlayerMove: asks for the player's next move
 - __isWinner: checks if the current player is a winner
 - __isBoardFull: checks if there is no more space left on the board
 - __showScores: shows the players' score

**Main Module**
The main code creates a TicTacToe object and contains two loops, one of them being the main loop  repeat games and one inner loop to go through players' moves by calling playNext method
When a game is complete, it uses playAgain function to ask use if they want to play a new game.