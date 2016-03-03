# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    """
    secretWord = string of characters making up a word
    lettersGuessed = list of letters that have been guessed
    
    returns a boolean: True if all letters of the secretWord are in lettersGuessed
                       False if otherwise
                       
    """
    
    Chars_in_Word = False
    
    for char in secretWord:
        if char in lettersGuessed:
            Chars_in_Word = True
        else:
            Chars_in_Word = False
            break
    
    return Chars_in_Word



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    Guessed_Word = ''
    
    for char in secretWord:
        if char in lettersGuessed:
            Guessed_Word += char
        else:
            Guessed_Word += ' _ '
    
    return Guessed_Word
        


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''

    Available_Letters = ''
    
    for letter in string.ascii_lowercase:
        if letter not in lettersGuessed:
            Available_Letters += letter
    
    return Available_Letters
    
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    
    print ""
    print ""
    print "Ready to play a game of Hangman?"
    print "I am thinking of a word that is " + str(len(secretWord)) + " letters long."
    print "-------------"
    
    lettersGuessed = []
    guessesLeft = 8
    
    while isWordGuessed(secretWord, lettersGuessed) == False and guessesLeft > 0:
        print "You have " + str(guessesLeft) + " guesses left."
        print "Available letters: " + getAvailableLetters(lettersGuessed)
        letter = raw_input("Please guess a letter: ").lower()
        if letter in lettersGuessed:
            print "Oops! you've already guessed that letter:",
        else:
            lettersGuessed.append(letter)
            if letter in secretWord:
                print "Good guess:",
            else: 
                guessesLeft -= 1
                print "Oops! That letter is not in my word:",
        print getGuessedWord(secretWord, lettersGuessed)
        print "-------------"
    
    if isWordGuessed(secretWord, lettersGuessed) == True:
        print "Congratulations! You won!"
    else:
        print "Sorry, you ran out of guesses. The word was " + secretWord + "."
        
        
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
