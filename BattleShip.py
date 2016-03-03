# -*- coding: utf-8 -*-
# Import function to generate a random integer
from random import randint

# Create the playing board
board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    """
    input: board is a list of equal sized lists of single characters to be printed
           for use as a playing board
    output: print the lists of characters in rows to the screen
    """
    for row in board:
        print " ".join(row)

# Welcome and print the playing field
print "Let's play Battleship!"
print_board(board)

def random_row(board):
    """
    generate a random list index (row) for the playing board
    """
    return randint(0, len(board) - 1)

def random_col(board):
    """
    generate a random list index (column) for the playing board
    """
    return randint(0, len(board[0]) - 1)

# Determine a random location for the ship in the game in reference to a playing board location
ship_row = random_row(board)
ship_col = random_col(board)

# Allow 4 turns or guesses as to the location of the ship
for turn in range(4):
    
    # Accept the user's input/guess data
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))
    
    # If the guess is correct, indicate and end the game
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break
    # Else the guess is incorrect: 
    else:
        # Check data validity - indicate the problem if out-of-limits guess,
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        # Check if guess was already made at that location
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        # Indicate a missed guess and print the board
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
            print_board(board)
        # Notify user of the current Turn
        print "Turn", turn + 1
        # Check to see if the game is over
        if turn == 3:
            print "Game Over"
            
            """
            Extra Credit
You can also add on to your Battleship! program to make it more complex and fun to play. 
Here are some ideas for enhancements—maybe you can think of some more!
- Make multiple battleships: 
    you'll need to be careful because you need to make sure that you don’t place 
    battleships on top of each other on the game board. You'll also want to make 
    sure that you balance the size of the board with the number of ships so the 
    game is still challenging and fun to play.
- Make battleships of different sizes: 
    this is trickier than it sounds. All the parts of the battleship need to be 
    vertically or horizontally touching and you’ll need to make sure you don’t 
    accidentally place part of a ship off the side of the board.
- Make your game a two-player game: 
    Use functions to allow your game to have more features like rematches, 
    statistics and more!
            """