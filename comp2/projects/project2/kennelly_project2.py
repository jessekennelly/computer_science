"""
Welcome to Wordle! You have six chances to guess the five-letter word.
A letter G means you got that letter correct and in the right position.
A letter Y means you matched that letter, but it is in the wrong position.
A letter B means that letter does not appear in the correct word.
"""
import random
words = []

with open("usaWords.txt", "r") as file:
    for line in file:
        word = line.rstrip()
        #populates list with words over 5 letters
        if len(word) == 5:
            words.append(word)
#creates random number for random index
number = random.randint(0, len(words))
newWord = words[number]

#iterates over number of guesses
for i in range(6):
    guess = input("What is your guess? ")
    guess = guess.lower()
    #if guess is below or above 5 letters, it asks for another input
    while len(guess) != 5:
        print("Word must be 5 letters")
        guess = input("What is your guess? ")
        guess = guess.lower()
    #if the word they inputted was not a real word, then it will ask for another input
    while guess in words == False:
        print("That is not a five letter word in our dictionary")
        guess = input("What is your guess? ")
        guess = guess.lower()
    hint = []
    hintWord = ""
    for j in range(len(guess)):
        #if the letter at the guessed word is equal to the letter of the wordle, then it displays 'G'
        if guess[j] == newWord[j]:
            hint.append("G")
        #if the letter is in the wrong spot but still in the word, it displays 'Y'
        elif guess[j] in newWord:
            hint.append("Y")
        else:
            #if its not in it at all, it displays 'G'
            hint.append("B")
        #joins hints together into a string
        hintWord = ' '.join([str(item) for item in hint])
    print(f"Guess {i+1}: {guess}   {hintWord}")
    #if the guess is the word, then it displays win message
    if guess == newWord:
        print(f"You win. You got it in {i+1} guesses")
        break

#at the end of the loop if they havent gotten it, it displays lose message
if i == 5:
    print("You lose, you did not guess the word in 6 guesses")