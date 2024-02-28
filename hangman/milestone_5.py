import random


class Hangman:
    '''
    This class contains the code needed to run the play_function below for a 'Hangman' style game. 

    It selects a random word from a given list.
    The user then guesses letters and the code checks to see if they are in the selected word.
    The code keeps track of letters guessed as well as showing the user their progress of guessing the word so far.
    The code also checks the number of lives the user has left.

    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_of_guesses: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
    '''
    def __init__(self, word_list, num_lives):
        '''
        This function uses the __init__ method to set up the game for the user.

        It selects a random word from the list given.
        It creates a list of _ which is the same length as the word chosen to keep track of the users progress guessing the word.
        It finds number of unique letters that need to be guessed.
        It creates an empty list that will keep track of the letters the user has guessed already.
        '''
        self.num_lives = num_lives
        self.word_list = word_list
    
        self.word = random.choice(self.word_list)

        self.word_guessed = ["_"] * len(self.word)

        self.num_letters = len(set(self.word))

        self.list_of_guesses = []
    
    def check_guess(self, guess):
        '''
        This function checks to see if the user's guess is in the word.

        If the input from the user is not in the word, the user is asked to try again and loses a life.
        If the letter guessed is in the word, the user is shown their progress.

        Parameters:
        ----------
        guess: str
            The guess to be checked
        '''
        guess = guess.lower()
        
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for g in range(len(self.word)):
                if self.word[g] == guess:
                    self.word_guessed[g] = guess
            self.num_letters -= 1
            print(f"Your progress so far: {self.word_guessed}.")

        else:
            self.num_lives -= 1
            print(f"Sorry. {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")
            print(f"Your progress so far: {self.word_guessed}.")

    def ask_for_input(self):
        '''
        This function asks the user to guess a letter.

        The user inputs a letter. If the input is not a single letter or they have already guessed that letter, they asked to input another letter.
        Once the input is valid, the check_guess function runs and the guessed letter is added to the list of guesses.
        '''
        while True:
            guess = input("Please guess a single letter: ")
            if guess.isalpha() == False or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break


def play_game(word_list):
    '''
    This function runs the code to play the hangman game.

    In this function we have chosen the number of lives to be 5 and will need a word_list to be defined outside of the function.
    The function runs through the Hangman class. It continues to run until the user's lives reach 0, when they are told they have lost the game or if they have guessed the word and won the game.
    '''
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        elif game.num_lives != 0 and game.num_letters == 0:
            print("Congratulations! You won the game.")
            break


if __name__ == "__main__":
    word_list = ["apple", "banana", "cherry", "mango", "kiwi", "fig"]

    play_game(word_list)



