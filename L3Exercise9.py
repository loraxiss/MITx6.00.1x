# Lesson 3 Problem 9 FingerExercise
# This is a program to guess a secret number between 0 and 100
# first initialize the variables
guess = 0
lower_limit = 0
upper_limit = 100
user_feedback = ''

#Ask for user involvement
print('Please think of a number between 0 and 100!')
while (user_feedback != 'C' and user_feedback != 'c'):
    #calculate the guess
    guess = lower_limit + (upper_limit - lower_limit)/2
    #Ask for user feedback regarding the guess
    print('Is your secret number ' + str(guess) + '?')
    user_feedback = raw_input('Enter "h" to indicate the guess is too high. Enter "l" to indicate the guess is too low. Enter "c" to indicate I guessed correctly.')
    #change the limits based on the user feedback about the guess. Accept either small or capitol letters as feedback
    if (user_feedback == 'h' or user_feedback == 'H'):
        upper_limit = guess
    elif (user_feedback == 'l' or user_feedback == 'L'):
        lower_limit = guess
    #if the user indicates the guess is correct, print game over and while loop ends
    elif (user_feedback == 'c' or user_feedback == "C"):
        print('Game over. Your secret number was: ' + str(guess))
    #if the user feedback is invalid, indicate invalid and repeat guest/request
    else:    
        print('Sorry, I did not understand your input.')


