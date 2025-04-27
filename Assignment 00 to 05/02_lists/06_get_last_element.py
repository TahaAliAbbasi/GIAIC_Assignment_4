def get_lst():

    """ Prompts the user to enter one element of the list at a time and returns the resulting list. """
    lst = []
    elem = input("Please enter an element of the list or press enter to stop. ") 

    while elem != "":
        lst.append(elem) 
        elem = input("Please enter an element of the list or press enter to stop. ")
        return lst 

def get_last_element(lst):
    print(lst[-1])

def main():
    lst = get_lst() 
    get_last_element(lst)



# Takes the length of the list and minuses 1 since they are zero-indexed (we start counting at 0)
# print(lst[len(lst) - 1])

# The line below works too!!
# print(lst[-1]) 

if __name__ == '__main__':
    main()