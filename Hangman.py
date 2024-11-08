import random

from hangman_words import word_list
from hangman_art import stages, logo

# Set lives equal to 6
lives = 6

# Printing the Hangman Logo
print(logo)

# Choosing a random word from the word list
chosen_word = random.choice(word_list)
print(chosen_word)

# Creating a placeholder which shows the same of number of blanks "_" as the number of letters in the chosen word
placeholder = ""
# Fetching the length of the chosen word
word_length = len(chosen_word)
# `for` loop to add the same number of blanks as the number of letters in the chosen word
for position in range(word_length):
    placeholder += "_"
print(placeholder)

# Fetching the guess from the user and lowercasing it to match the chosen word
# Using a while loop to let user guess again and again until the guess is correct
game_over = False

# We used this correct letters list to store the correct letters guessed by the user
correct_letters = []

while not game_over:
    print(f"*************** {lives} / 6 LIVES LEFT *****************")
    guess = input("Guess a letter: ").lower()

# If the guessed letter is already in the correct_letters list, print a message to the user that the letter has already been guessed
    if guess in correct_letters:
        print(f"You have already guessed {guess}")

# Creating a "Display" which will show the guessed letters in the correct positions and the rest of the letters as "_"
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

# If the guessed letter is not in the chosen word, reduce the lives by 1
    if guess not in chosen_word:
        lives -=1
# If the guessed letter is not in the chosen word, print a message to the user that the letter is not in the word and reduce the lives by 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            game_over = True
# If the user has no lives left, print a message to the user that they have lost the game and return the correct word to the user
            print(f"**************** IT WAS {chosen_word}! YOU LOSE *******************")

# Winning condition - if the display does not contain any "_", the user has guessed all the letters correctly
    if "_" not in display:
        game_over = True
        print("**************** YOU WIN *******************")

# Printing the ASCII Art Stages of the game, which shows the lives left
    print(stages[lives])

