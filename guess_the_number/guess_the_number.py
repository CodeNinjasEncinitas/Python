import random

while True:
    print("")
    print("------New Game------")
    min = int(input("Enter a minimum: "))
    max = int(input("Enter a maximum: "))
    secret = random.randint(min, max)
    print("A secret number has been chosen!")
    guess = int(input("What do you think it is? "))
    print("The secret number was... " + str(secret))
    if secret == guess:
        print("You guessed right!")
    else:
        print("Fail!!!")