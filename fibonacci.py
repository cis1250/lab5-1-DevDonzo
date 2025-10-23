#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)

def get_terms_input():
    """
    prompts the user for the number of fibonacci terms, validates that it
    is a positive integer, and returns it.
    """
    while True:
        try:
            # get user input
            user_input = input("How many terms of the Fibonacci sequence do you want? ")
            # try to convert to an int
            num_terms = int(user_input)
            
            # check if the integer is positive
            if num_terms > 0:
                return num_terms  # good input, return it
            else:
                print("Error: Please enter a positive integer.")
        except ValueError:
            # handle cases where input is not a number
            print("Error: Invalid input. Please enter a whole number.")

def generate_fibonacci(n):
    """
    generates the fibonacci sequence up to 'n' terms and returns it as a list.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]

    # initialize the sequence list and the first two numbers
    sequence = []
    a, b = 0, 1
    
    # use a for loop to generate the sequence
    for _ in range(n):
        sequence.append(a)
        # update the next two numbers in the sequence
        a, b = b, a + b
        
    return sequence

def print_sequence(seq):
    """
    prints the given sequence in a readable, space-separated format.
    """
    if not seq:
        print("The sequence is empty.")
        return
        
    print("\nHere is the Fibonacci sequence:")
    # convert all numbers in the list to strings and join with a space
    print(" ".join(map(str, seq)))

def main():
    """
    main function to run the fibonacci program.
    """
    terms = get_terms_input()
    sequence = generate_fibonacci(terms)
    print_sequence(sequence)

# standard boilerplate to run the main() function
if __name__ == "__main__":
    main()
