# roll2Dice.py
# by _______
# Write a program the simulates the rolling of 2 dice
# NOTE: 
# pay close attention to the flowchart in the learning log
# or on my GitHub repo: https://github.com/HundredVisionsGuy/Roll2Dice-Challenge/blob/master/Roll2Dice.jpg

# import statements
import _______

# Write function defintion: checkRoll()
___ _______(__, __):
    """ _____________ """
    # set total of die1 and die2
    _____ = _____ _ _____

    # set msg to result of the dice roll
    msg = "_____" + die1 + "_____" _ ___ _ 
    msg += " for a _____" + _____

    # check for output
    if _____ __ _____:
        # Is total a 2?
        msg += "_______________"
    ____ _____ __ _____:
        # Is total a 12?
        msg += "_______________"
    ____ _____ __ _____:
        # Is total a 7?
        msg += "_______________"
    ____: 
        # Otherwise, it's a draw
        msg += "_______________"

    # Make sure it returns a value
    ______ ___

if __name__ == '__main__':
    # Call the function in here if you want to test it
    # Make sure it's indented
    # set d1 to random number between 1 and 6
    _____ = random._______(_______, _______)
    
    # set d2 to random number between 1 and 6
    _____ = random._______(_______, _______)

    # set output to roll2Dice() sending it the two dice values
    _____ = _______(_______, _______)

    # print output 
    print(_____)

    # Thank the user
    _______________

    # Quit gracefully
    input("Press enter to quit")