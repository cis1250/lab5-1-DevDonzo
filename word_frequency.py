#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)

import re

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    """
    checks if a text string qualifies as a valid sentence.
    """
    # check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # check for starting with a capital letter
    if not text[0].isupper():
        return False

    # check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True

def get_sentence():
    """
    prompts the user to enter a sentence and validates it using is_sentence().
    """
    while True:
        sentence = input("Please enter a sentence: ")
        if is_sentence(sentence):
            return sentence
        else:
            print("Invalid input. A sentence must start with a capital letter, "
                  "contain words, and end with '.', '?', or '!'.")

def calculate_frequencies(sentence):
    """
    calculates the frequency of each word in a sentence.
    returns two lists: one of unique words and one of corresponding frequencies.
    """
    # create empty lists to store words and their frequencies
    unique_words = []
    frequencies = []
    
    # prepare the string: make it lowercase and remove all punctuation
    # this ensures "Word." and "word" are counted as the same.
    cleaned_sentence = sentence.lower()
    cleaned_sentence = re.sub(r'[^\w\s]', '', cleaned_sentence)
    
    # split the cleaned sentence into a list of words
    word_list = cleaned_sentence.split()
    
    # iterate through the list of words
    for word in word_list:
        # check if the word is already in our list of unique words
        if word in unique_words:
            # if it exists, find its index
            index = unique_words.index(word)
            # update its frequency in the corresponding list
            frequencies[index] += 1
        else:
            # if it's a new word, append it to the words list
            unique_words.append(word)
            # append a frequency of 1 to the frequencies list
            frequencies.append(1)
            
    return unique_words, frequencies

def print_frequencies(words, frequencies):
    """
    prints the word frequencies in a readable format.
    """
    print("\nWord Frequencies:")
    # iterate through the lists using their indices
    for i in range(len(words)):
        print(f"{words[i]}: {frequencies[i]}")

def main():
    """
    main function to control the program flow.
    """
    # get the input
    sentence = get_sentence()
    
    # process the input
    words, freqs = calculate_frequencies(sentence)
    
    # display the result
    print_frequencies(words, freqs)

# standard check to run main()
if __name__ == "__main__":
    main()
