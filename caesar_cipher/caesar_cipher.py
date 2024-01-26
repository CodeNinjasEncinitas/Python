message = input("Enter some text: ")
key = int(input("Enter a key number: "))

alphabet = list("abcdefghijklmnopqrstuvwxyz")

def encrypt(text):
    string = ""
    for letter in text:
        index = alphabet.index(letter)
        index += key
        while index > 25:
            index -= 26
        while index < 0:
            index += 26
        string += alphabet[index]
    return string

def decrypt(text):
    string = ""
    for letter in text:
        index =  alphabet.index(letter)
        index -= key
        while index > 25:
            index -= 26
        while index < 0:
            index += 26
        string += alphabet[index]
    return string  

encrypted = encrypt(message)
print("Encrypted Message: " + encrypted)
decrypted = decrypt(encrypted)
print("Decrypted Message: " + decrypted)


