# import random

# word_list = ["apple", "banana", "cherry", "grape", "orange"]
# word = random.choice(word_list)

# while True:
#     guess = input("Guess a letter: ")
#     if len(guess) == 1 and guess.isalpha():
#         break
#     else:
#         print("Invalid letter. Please, enter a single alphabetical character.")

# if guess in word:
#     print(f"Good guess! '{guess}' is in the word.")
# else:
#     print(f"Sorry, '{guess}' is not in the word. Try again.")

# 

import random

word_list = ["apple", "banana", "cherry", "grape", "orange"]
word = random.choice(word_list)

def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print(f"Good guess! '{guess}' is in the word.")
    else:
        print(f"Sorry, '{guess}' is not in the word. Try again.")

def ask_for_input():
    while True:
        guess = input("Guess a letter: ")
        if len(guess) == 1 and guess.isalpha():
            check_guess(guess)  # Keep checking the guess inside the loop
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

ask_for_input()

