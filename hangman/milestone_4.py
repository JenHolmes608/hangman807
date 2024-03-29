import random

class Hangman:
    '''
    This class contains the code needed to run the play_function below for a 'Hangman' style game. 

    It selects a random word from a given list.
    The user then guesses letters and the code checks to see if they are in the selected word.
    The code keeps track of letters guessed as well as showing the user their progress of guessing the word so far.
    The code also checks the number of lives the user has left.
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
        '''
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for g in self.word:
                if g == guess:
                    guess_index = self.word.find(guess)
                    self.word_guessed[guess_index] = guess
            self.num_letters -= 1

        else:
            self.num_lives -= 1
            print(f"Sorry. {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")

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
    
