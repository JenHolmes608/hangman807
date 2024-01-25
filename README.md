# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

In #milestone_2 #milestone_3 and #milestone_4 I have written sections of code that I have then put together to create the full code for the Hangman game.

#milestone_2: This file defines a list of fruit and selects one at random.
Then it asks the user to input a single letter and checks that the input is a single letter.

#milestone_3: This file includes two functions. A word is chosen randomly from a list. The first function works out if a guessed letter is within the chosen word. The second function asks the user to choose a letter and then runs the first function to check the guess.

#milestone_4: This file creates the Hangman class. It uses the __init_ method to introduce relavent attributes and uses methods that ask the user to guess a letter. It keeps track of the letters the user has guessed.

#milestone_5: This file contains a full working version of the Hangman code. It uses a lot of the code from #milestone_4 but adds a function outstide of the Hangman class which rund the code to play the Hangman game.


To implement running the project, git clone the repo and run the file in the terminal. Python is required:

```
python milestone_5.py
```
To run the project, a word list must be defined, then, using the code from #milestone_5 you can define the Hangman class and play_game function. The play game function must then be called using the word list that has been created. Note that the number of lives can be altered in the play_game function.
The project could be improved if a large list of words was already imported so that it doesn't need to be defined before running the play_game function. When the player reache one life left, they are told the have 1 lives remaining, this could also be fixed.