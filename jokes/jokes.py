import random

file_path = './jokes.txt'

while True:
    print("Welcome to the Joke Machine!")
    print("Enter 1 to share a joke")
    print("Enter 2 to hear a joke")
    user_input = int(input("Enter your selection: "))
    if user_input == 1:
        joke = input("Type your joke and press Enter: ")
        # save joke to jokes.txt
    elif user_input == 2:
        with open(file_path, 'r') as file:
            # Use the readlines() method to read all lines into a list
            lines = file.readlines()
            total_jokes = len(lines)
            random_number =  random.randint(0, total_jokes-1)
            print(lines[random_number])
    else:
        print("Bad Input... Restarting")
