import random

while True:
    # print a divider for readability
    print("----------------------------")
    # collect user input to pause the program until Enter is pressed
    user_input = input("Press Enter to roll the dice")
    # print an empty line for readability
    print(" ")
    # generate a random number from 1-6 (inclusive of min and max values)
    roll = random.randint(1, 6)
    # convert the value to a String so it can be printed
    roll =  str(roll)
    # print out the result
    print("You rolled a " + roll)
    
