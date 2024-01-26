# we need a reference alphabet to make sure people guess actual letters
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# an empty list that will store correctly guessed letters
correct_guesses = []
# an empty list that will store wrongly guessed letters
wrong_guesses = []
# a dictionary to keep track of which body parts have been drawn so far, initially nothing so all false
body = {
  "head": False,
  "torso": False,
  "leftarm": False,
  "rightarm": False,
  "leftleg": False,
  "rightleg": False
}
# create an empty string that stores what's been guessed correctly
guessed_string = ""

# player 1 will enter a word before the game starts that player 2 can try to guess
word = input("Enter a word or phrase: ")
# main game loop
while True:
    print("----------------------------------------------")
    empty_letter_spaces = ""
    for letter in word:
        if letter == ' ':
            empty_letter_spaces += ' '
        elif letter in correct_guesses:
            empty_letter_spaces += letter
        else:
            empty_letter_spaces += "_"
    print("Secret Word: " + empty_letter_spaces)
    # check for win game condition
    if empty_letter_spaces == word:
        # print YOU WIN and break the While Loop so the game stops
        print("YOU WIN!")
        break
    # check for game over condition
    if len(wrong_guesses) == 6:
        # print GAME OVER and break the While Loop so the game stops
        print("GAME OVER!")
        break
    guess = input("Guess a letter: ")
    # make sure the letter guessed exists in the alphabet 
    if guess.lower() in alphabet:
        # is the letter that was guessed in the secret word/phrase?
        if guess in word:
            # if so, append it to our list of correctly guessed letters
            correct_guesses.append(guess)
        # if the letter that was guessed isn't in the word
        else:
            # add it to our list of wrong guesses
            wrong_guesses.append(guess)
            # "draw" the next body part that needs to be drawn based on counting how many have been taken so far
            if len(wrong_guesses) == 1:
                body['head'] = letter
            if len(wrong_guesses) == 2:
                body['torso'] = letter
            if len(wrong_guesses) == 3:
                body['leftarm'] = letter
            if len(wrong_guesses) == 4:
                body['rightarm'] = letter
            if len(wrong_guesses) == 5:
                body['leftleg'] = letter
            if len(wrong_guesses) == 6:
                body['rightleg'] = letter
    else:
        print("You didn't guess a letter...")
    # print out the body parts and whether it's True they have been drawn
    for part in body:
        print(part + ": " + str(body[part]))
    # print out all of the correct and wrong letters guessed so far
    print("Correct Guesses:" + str(correct_guesses))
    print("Wrong Guesses:" + str(wrong_guesses))
    
    
    




