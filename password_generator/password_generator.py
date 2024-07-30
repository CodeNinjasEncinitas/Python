import random

allowed_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

allowed_characters = list(allowed_characters)


def generatePassword(length):
    password_string = ""
    for i in range(0, length):
        password_string += random.choice(allowed_characters)
    return password_string 

while True: # forever loop
    print("----------------------------------------------") 
    user_input = input("How long should the password be?  ") 
    length = int(user_input)
    password = generatePassword(length)
    print("Password:  " + password) 