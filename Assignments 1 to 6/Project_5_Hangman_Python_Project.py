import random
import string

words = ["mango", "banana", "grapes", "cherry", "watermelon", "apple"]

def get_valid_word(words):
    return random.choice(words).upper()  # Ensure uppercase for consistency

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # Letters in the word
    alphabet = set(string.ascii_uppercase)  # Standard uppercase alphabet
    attempts = 6  # Limit the number of wrong guesses
    used_letters = set()  # Letters guessed

    while attempts > 0 and len(word_letters) > 0:
        # Letters used
        print("\nYou have used these letters:", ' '.join(used_letters))
        print(f"You have {attempts} attempts remaining.")

        # Display current word progress
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print('Current word:', ' '.join(word_list))

        # Get user input
        user_letter = input('Guess a letter: ').upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                attempts -= 1  # Deduct an attempt for incorrect guesses
                print("Incorrect guess!")

        elif user_letter in used_letters:
            print("You have already used that letter. Try again.")

        else:
            print("Invalid character. Please enter a valid letter.")

    # End game message
    if len(word_letters) == 0:
        print(f"Congratulations! You guessed the word: {word}")
    else:
        print(f"Game over! The word was: {word}")

hangman()