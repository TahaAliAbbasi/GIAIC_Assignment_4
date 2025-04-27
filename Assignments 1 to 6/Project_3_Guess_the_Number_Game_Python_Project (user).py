import random
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c' and low != high:
        guess = random.randint(low,high)
        feedback = input(f"Is {guess} too high(h) , too low (l) or correct (c).")
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f"Yay! The computer has guessed your number,{guess},correctly!")       

start = input("Enter any number between 1 and 10 and computer will guess it : ")
computer_guess(10)