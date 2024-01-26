import random

while True:
    # print a divider for readability
    print("----------------------------")
    # collect user input to pause the program until Enter is pressed
    user_input = input("Press Enter to flip the coin")
    # print an empty line for readability
    print(" ")
    # generate a random value that's a 0 or a 1
    value = random.randint(0, 1)
    # if it's a 0 make it heads
    if value == 0:
        value = "HEADS"
    # tails if it was 1
    if value == 1:
        value = "TAILS"
    # print the result
    print("You flipped a coin and got a " + value)
    
