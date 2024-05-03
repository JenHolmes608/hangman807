Hangman is a classic word guessing game in which one player thinks of a word and the other player tries to guess it letter by letter within a certain number of attempts.

This project is an implementation of the Hangman game in Python, where the computer randomly selects a word from a predefined list and the user attempts to guess it.

Milestones
Milestone 2: In this stage, a list of fruit is defined, and the program selects one fruit at random. Then, it prompts the user to input a single letter and checks if the input is valid.
Milestone 3: This file includes two functions. The first function randomly chooses a word from a list, and the second function checks if a guessed letter is present in the chosen word.
Milestone 4: The Hangman class is created in this file. It utilizes the _init method to introduce relevant attributes and incorporates methods that prompt the user to guess a letter while keeping track of the letters guessed.
Milestone 5: This file contains a fully working version of the Hangman game. It builds upon the code from Milestone 4 but adds a function outside of the Hangman class to run the game.
Installation
To run the project, follow these steps:

Clone the repository:
bash
Copy code
git clone https://github.com/JenHolmes608/hangman807.git
Navigate to the project directory:
bash
Copy code
cd hangman807
Run the Python file in the terminal:
bash
Copy code
python milestone_5.py
Usage
Once the project is set up and running, the user can play the Hangman game by guessing letters to uncover the hidden word. The number of lives can be adjusted within the play_game function. However, note that defining a word list before running the game is necessary. Improvements could include importing a large word list to eliminate the need for defining one manually and fixing the message when the player reaches one life remaining.

Feel free to contribute to this project by adding features, fixing bugs, or suggesting improvements!
