# Hangman

## Table of Contents
1. [Project Description](#project-description)  
   - [Learnings](#learnings) 
2. [Installation Instructions](#installation-instructions)  
3. [Usage Instructions](#usage-instructions)  
4. [File Structure of the Project](#file-structure-of-the-project)  
5. [License Information](#license-information)  

## Project Description
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.
This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

### Learnings 
- Object-Oriented Programming (OOP) in Python: How to define classes, methods, and instantiate objects.
- Function Design: How to design methods for different game operations.
- User Input Handling: How to process and validate user input.
- Game Flow Control: Implementing game logic with loops, conditionals, and methods to control the game's progression.

## Installation Instructions
To run the Hangman game locally, follow these steps:

### Step 1: Install Dependencies
This project does not require any external dependencies, as it only uses built-in Python modules. Ensure you have Python 3 installed on your system.

### Step 2: Run the Script
- Clone the repository
- Run python milestone_5.py

## Usage instructions
Once you run the script, the game will start in the terminal. Here's how to play:

- The game will randomly select a word from the provided word list.
- The player will be asked to guess a letter.
- If the guessed letter is in the word, it will be revealed in the word display.
- If the guessed letter is not in the word, the player will lose one life.
- The player starts with 5 lives. If all lives are lost before the word is guessed, the player loses.
- The game continues until the player either guesses the entire word correctly or loses all their lives.
- To exit the game, simply close the terminal or stop the execution.

## File structure of the project
hangman-game/
- milestone_5.py          # Main script with the Hangman game logic
- milestone_4.py          # Previous version of the game (for reference)
- milestone_3.py          # Milestone 3 (for reference)
- milestone_2.py          # Milestone 2 (for reference)
- README.md               # Project documentation


## License information
