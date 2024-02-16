import random
import time

# a string containing the character we will allow in a password
allowed_characters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!#$%&'()*+,-./:;<=>?@[\]^_`{|}~")

def generatePassword(length):
    password_string = ""
    for i in range(0, length):
        password_string += random.choice(allowed_characters)
    return password_string

while True:
    print("----------------------------------------------")
    user_input = input("How long should the password be?  ")
    length = int(user_input)
    password = generatePassword(length)
    print("Password:  " + password)

# try this after (comment out the while loop above)
# while True:
#     password = generatePassword(150)
#     print(password)
#     time.sleep(.01)