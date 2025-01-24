class Hangman:
    def __init__(self, word_list, num_lives=5):
        import random
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))  # Count unique letters
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        if guess in self.word:
            print(f"Good guess! '{guess}' is in the word.")
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, '{guess}' is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        while True:
            guess = input("Guess a letter or type 'guess' to guess the entire word: ").lower()

            if guess == "guess":
                full_word_guess = input("Enter your guess for the full word: ").lower()
                if full_word_guess == self.word:
                    self.word_guessed = list(self.word)  # Reveal the whole word
                    print("Congratulations! You guessed the word correctly!")
                    break
                else:
                    self.num_lives -= 1
                    print(f"Sorry, '{full_word_guess}' is not the word.")
                    print(f"You have {self.num_lives} lives left.")
            elif len(guess) == 1 and guess.isalpha():  # Only allow single letter guesses
                if guess in self.list_of_guesses:
                    print(f"You already tried the letter '{guess}'. Try another letter.")
                else:
                    self.list_of_guesses.append(guess)
                    self.check_guess(guess)
                    break
            else:
                print("Invalid input. Please enter a single alphabetical character or 'guess' to guess the entire word.")

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)

    while True:
        if game.num_lives == 0:
            print(f"You lost! The word was: {game.word}")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations. You won the game!")
            break

# Example word list
word_list = ["apple", "banana", "grape", "orange", "strawberry"]
play_game(word_list)
