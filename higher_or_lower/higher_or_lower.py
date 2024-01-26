import random
# generate a random number in range 1-100
number = random.randint(1, 100)
print("Computer chose a number")
# set a total guesses variable to 0 to keep track
total_guesses = 0
while True:
    # collect input for player's guess
    guess = input("Enter a guess: ")
    # see if the guess can be converted to an int
    try:
        guess = int(guess)
    # if it can't, then tell the user it was bad input and skip the rest of this loop
    except:
        print("You need to enter a number")
        continue
    # print Higher or Lower depending on the guess and the number
    if guess < number:
        print("Higher")
    elif guess > number:
        print("Lower")
    # if the guess is equal to the number print You Win and break the while loop to end the game
    else:
        print("You win!")
        print("Total Guesses: " + str(total_guesses))
        break
    # if the player didn't guess the number correctly, the following code will run
    total_guesses += 1
    print("Total Guesses: " + str(total_guesses))
    # divider for readability
    print("------------------------------")