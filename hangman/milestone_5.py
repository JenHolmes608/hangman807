import random

class Hangman:
    def __init__(self, word_list, num_lives):
        self.num_lives = num_lives
        self.word_list = word_list
    
        self.word = random.choice(self.word_list)

        self.word_guessed = [*self.word]
        for i in range(len(self.word_guessed)):
            if self.word_guessed[i] != "_":
              self.word_guessed[i] = "_"

        self.num_letters = len(set(self.word)) - len(set(self.word_guessed)) + 1

        self.list_of_guesses = []
    
    def check_guess(self, guess):
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
        while True:
            guess = input("Please guess a single letter: ")
            if guess.isalpha() == False and len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        elif game.num_lives != 0 and game.num_letters == 0:
            print("Congratulations, you won the game.")
            break

word_list = ["apple", "banana", "cherry", "mango", "kiwi"]

play_game(word_list)


