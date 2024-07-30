alphabet_vowels = list("aeiou") # create a list of all the vowels in the alphabet
alphabet_consonants = list("bcdfghjklmnpqrstvwxyz") # create a list of all the consonants in the alphabet

while True:
    word = input("Enter a word: ") # collect user input for any WORD

    # initialize counter variables to keep track of the number of vowels and consonants in the user input word
    total_vowels = 0
    total_consonants = 0
    #
    vowels_list = []
    consonants_list = []

    for letter in word:
        if letter in alphabet_vowels:
            total_vowels += 1
            vowels_list.append(letter)
        elif letter in alphabet_consonants:
            total_consonants += 1
            consonants_list.append(letter)

    text1 = f"Your word contains {total_vowels} vowels... {vowels_list}"
    print(text1)
    text2 = f"Your word contains {total_consonants} consonants... {consonants_list}"
    print(text2)
    print("-----------------------------------------------------------")
