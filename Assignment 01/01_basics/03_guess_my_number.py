import random

def main():
    # Generate the secret number at random!
    secret_number: int = random.randint(1, 99)
    number_of_guesses = 1
    
    print("I am thinking of a number between 1 and 99...")
    
    # Get user's guess
    guess = int(input("Enter a guess: "))
    # True if guess is not equal to secret number
    while guess != secret_number:
        number_of_guesses = number_of_guesses + 1
        if guess < secret_number:  # If-statement is True if guess is less than secret number
            print("Your guess is too low")
        else:
            print("Your guess is too high")
            
        print() # Print an empty line to tidy up the console for new guesses
        guess: int = int(input("Enter a new guess: "))  # Get a new guess from the user
        
    print("Congrats! The number was : " + str(secret_number) + " You guessed correct number in " +str(number_of_guesses) + " Guesses.")
    
if __name__ == '__main__':
    main()
