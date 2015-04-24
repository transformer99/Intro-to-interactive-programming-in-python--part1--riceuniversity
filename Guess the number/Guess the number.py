# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import random
import simplegui
import math
 
# initialize global variables used in your code
secret_number = 0
num_range = 100
num_queue = 0
 
# helper function to start and restart the game
def new_game():
    # remove this when you add your code    
    global num_range
    global num_queue
    global secret_number
    
    secret_number = random.randrange(0, num_range)
    num_queue = int(math.ceil(math.log(num_range, 2)))
    
    print "New game. Range is from 0 to", num_range
    print "Number of remaining guesses is", num_queue, "\n"
 
 
# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global num_range
 
    num_range = 100
    
    new_game()
 
def range1000():
    # button that changes range to range [0,1000) and restarts
    global num_range
 
    num_range = 1000
    
    new_game()
    
def input_guess(guess):
    # main game logic goes here
    global num_queue
    global secret_number
    global num_range
    guess_check = 0
    try:
        guess_check = int(guess)
    except ValueError:
        print "You entered invalid characters:", guess
        print "The number your entered should just be number.\n"
        return
    
    if guess_check < 0 or guess_check >= num_range:
        print "You entered number is out of range!\n"
        return
    num_queue = num_queue - 1
        
    print "Guess was", guess_check
    print "Number of remaining guesses is", num_queue
    if num_queue > 0:
        if secret_number == guess_check:
            print "Correct!\n"
            if num_range == 100:
                range100()
            else:
                range1000()
        elif secret_number > guess_check:
            print "Higher!\n"
        else:
            print "Lower!\n" 
    else:
        if secret_number == guess_check:
            print "Correct!\n"
        else:
            print "You ran out of guesses. The number was", secret_number, "\n"
        if num_range == 100:
            range100()
        else:
            range1000()
                
# create frame
f = simplegui.create_frame("Guess the number", 200, 200)
 
# register event handlers for control elements
f.add_button("Range is [0, 100)", range100, 200)
f.add_button("Range is [0, 1000)", range1000, 200)
f.add_input("Enter a guess", input_guess, 200)
 
# call new_game and start frame
new_game()
 
# always remember to check your completed program against the grading rubric