def main():
    curr_value = int(input("\nPlease enter any number and i will double it untill it becomes greator than 100 : ")) # Takes input value from user

    while curr_value < 100: #continues untill users input becomes greator than 100
        curr_value = curr_value*2 # Doubles users value every time
        print(curr_value) # prints the value

if __name__ == '__main__':
    main()