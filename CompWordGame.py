from WordGame import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def isInHand(word, hand):
    """
    Returns True if word is entirely
    composed of letters in the hand. 
    Otherwise, returns False.

    Does not mutate hand.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    
    # Intialize Variables
    
    inHand = False
    checkHand = hand.copy()
    
    try: 
        for letter in word: #check that letter in hand, then decrement
            if checkHand[letter] > 0:
                inHand = True
                checkHand[letter] -=1
            else:
                inHand = False
                break
        return inHand
    except KeyError: # if a KeyError is raised in accessing the Hand, letter isn't in hand
        return False


def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """

    # Create a new variable to store the maximum score seen so far (initially 0)
    Best_Score = 0
    # Create a new variable to store the best word seen so far (initially None)  
    Best_Word = "None"
    # For each word in the wordList
    for word in wordList:
        # If you can construct the word from your hand
        if isInHand(word, hand):
            # Find out how much making that word is worth
            Word_Score = getWordScore(word, n)
            # If the score for that word is higher than your best score
            if Word_Score > Best_Score:
                # Update your best score, and best word accordingly
                Best_Score = Word_Score
                Best_Word = word
    # return the best word you found.
    return Best_Word
#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
     
    # Keep track of the total score
    total_score = 0
    
    # As long as there are still letters left in the hand:
    while calculateHandlen(hand) != 0:
        # Display the hand
        print "Current Hand: ",
        displayHand(hand)
        # Computer chooses word:
        word = compChooseWord(hand, wordList, n)
        # If the word is "None" 
        if word == 'None':
            # End the game (break out of the loop)
           break
        else:
            # print how many points the word earned, and the updated total score, in one line followed by a blank line
            total_score += getWordScore(word, n)
            print '"' + word + '"', "earned", getWordScore(word, n), "points. Total:", total_score, "points"
            print ""
            # Update the hand 
            hand = updateHand(hand, word) 
    
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    
    print "Total score: ", total_score

#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """

 # Initial Variables
    HAND = {}
    HAND_SIZE = 7           # size of hand
    
    print              # Print Blank Line
    
    # repeat the game until the user changes Game_Mode to "e" (end) and breaks the loop
    while True:
        # Initialize Game_Mode (new, replay, end) and Player (user, computer) Variable for each game
        Game_Mode = ""
        Player = ""
        
        # Get input from the user: new game, replay hand or end
        while Game_Mode not in ("n", "r", "e"):
            Game_Mode = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
            if Game_Mode not in ("n", "r", "e"):
                print "Invalid Command"
        
        # Set and check parameters based on the Game Mode selected
        # if user requests "e" (end) then exit the loop)
        if Game_Mode == "e":
            break
        # Check and load a new Hand if necessary
        elif Game_Mode == "n":
            HAND = dealHand(HAND_SIZE) 
        elif Game_Mode == "r" and HAND == {}:
            print "You have not played a hand yet. Please play a new hand first!"
        
        # If the Hand is loaded, play in user or computer mode as requested
        if HAND != {}:
            # Get input from the user as to the player: human or computer, loop until correct input
            while Player not in ("u", "c"):
                Player = raw_input("Enter u to have yourself play, c to have the computer play: ")
                if Player not in ("u", "c"):
                    print "Invalid Command"
            # Call the appropriate function based on whether the humam or computer is playing
            if Player == "u":
                playHand(HAND, wordList, HAND_SIZE)
            elif Player == "c":
                compPlayHand(HAND, wordList, HAND_SIZE)
       
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)

