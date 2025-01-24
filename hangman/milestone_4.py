import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        """
        Initializes the Hangman game with a random word, a list of underscores for each letter,
        and a set number of lives.

        :param word_list: List of possible words to choose from
        :param num_lives: Number of lives the player starts with
        """
        self.word = random.choice(word_list)
        self.word_guessed = ["_"] * len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.guesses_made = []

    def _update_word_guessed(self, guess):
        """
        Updates the word_guessed list with the correct guessed letters.
        
        :param guess: The letter guessed by the user
        """
        for index, letter in enumerate(self.word):
            if letter == guess:
                self.word_guessed[index] = guess
        self.num_letters -= 1

    def _process_incorrect_guess(self, guess):
        """
        Reduces lives when the guess is incorrect and prints a message.

        :param guess: The letter guessed by the user
        """
        self.num_lives -= 1
        print(f"Sorry, {guess} is not in the word.")
        print(f"You have {self.num_lives} lives left.")

    def _is_valid_guess(self, guess):
        """
        Validates if the guess is a single alphabetical character and not previously guessed.

        :param guess: The letter guessed by the user
        :return: True if the guess is valid, False otherwise
        """
        if not (guess.isalpha() and len(guess) == 1):
            print("Invalid letter. Please, enter a single alphabetical character.")
            return False
        if guess in self.guesses_made:
            print("You already tried that letter!")
            return False
        return True

    def check_guess(self, guess):
        """
        Checks whether the guessed letter is in the word, updating word_guessed and lives accordingly.

        :param guess: The letter guessed by the user
        """
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            self._update_word_guessed(guess)
        else:
            self._process_incorrect_guess(guess)

    def ask_for_input(self):
        """
        Asks the user for a valid guess and processes it.
        """
        while True:
            guess = input("Guess a letter: ")
            if self._is_valid_guess(guess):
                self.check_guess(guess)
                self.guesses_made.append(guess)
                break

    def display_word_guessed(self):
        """
        Prints the current state of the word_guessed list.
        """
        print("Current word:", " ".join(self.word_guessed))

# Example usage
word_list = ["apple", "banana", "cherry", "grape", "orange"]
game = Hangman(word_list)
game.ask_for_input()
game.display_word_guessed()
