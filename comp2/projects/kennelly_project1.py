"""
    Plays a game of Fermi Pico Bagels where the user tries to guess a three digit number with hints to the correct number and postition
    with each round
    Filename: kennelly_project1.py
    Author: Jesse Kennelly
    Date: 1/9/23
    Course: COMP1352
    Assignment: Project 1 - A Guessing Game
    Collaborators: None
    Internet Source: None
"""

import random

num = [str(random.randint(0,9)), str(random.randint(0,9)), str(random.randint(0,9))]
#checks to see if there are any duplicate numbers
while num[0] == num[1] or num[1] == num[2] or num[0] == num[2]:
    num = [str(random.randint(0,9)), str(random.randint(0,9)), str(random.randint(0,9))]

guesses = 1

while True:
    guess = input("What is your guess? ")

    #checks to see if there are any duplicate numbers in guess
    if guess[0] == guess[1] or guess[1] == guess[2] or guess[2] == guess[0]:
        print("Invalid guess. Cannot be same numbers")
        continue
    
    hint = []

    for i in range(3):
        #adds Fermi if the number and position are right
        if guess[i] == num[i]:
            hint.append('Fermi!')
        #adds Pico if number is in num but not in right spot
        elif guess[i] in num:
            hint.append('Pico!')
    #if no hints were added (no Pico and no Fermi) then it must be Bagels
    if len(hint) == 0:
        print('Bagels!')
    else:
        print(' '.join(hint))
    #guess counter
    guesses += 1

    #final check to see if all numbers are in correct spot
    if guess[0] == num[0] and guess[1] == num[1] and guess[2] == num[2]:
        print(f'You got it in {guesses} guesses')
        #breaks infinte loop once if is true
        break