word_list = ["apple", "banana", "grapes", "mango", "pineapple"]
print(word_list)

import random

word = random.choice(word_list)
print(word)


guess = input("Please enter a single letter: ")

if guess.isalpha() and len(guess) == 1:
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")