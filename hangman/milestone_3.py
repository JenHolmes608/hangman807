word_list = ["apple", "banana", "grapes", "mango", "pineapple"]

import random

word = random.choice(word_list)

def check_guess(guess):
   '''
   This function checks if the guessed letter is in the chosen word.
   '''
   guess = guess.lower()
   if guess in word:
     print(f"Good guess! {guess} is in the word.")
   else:
     print(f"Sorry. {guess} is not in the word. Try again.")

def ask_for_input():
  '''
  This function asks user to enter a single letter and checks it is a valid input. 

  If the input is valid, it runs the check_guess function.
  '''
  while True:
    guess = input("Please guess a single letter: ")
    if guess.isalpha() and len(guess) == 1:
      break
    else:
       print("Invalid letter. Please, enter a single alphabetical character.")
  check_guess(guess)

ask_for_input()
