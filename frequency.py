# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 1: Word Frequency
#
# NAME:         Giovanni ROsati
# ASSIGNMENT:   Project 3: Arrays & Maps

from operator import itemgetter
import string
import json

# Create a function word_frequencies that takes
# a string filename as a parameter and returns a
# dictionary mapping each word in the text file
# to the total number of times it occurs. All
# letters should be treated as lower case, and both
# punctuation and numbers should be ignored.
# Letters separated by apostrophes should be left together.
# Your solution may use string & file functions.
# Hint: see https://www.techiedelight.com/remove-punctuations-string-python/

punctuation_and_numbers = "—!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~0123456789"

# def preprocess_word(word):
#     word = word.lower()
#     word = word.replace("'", "")   # remove apostrophes
#     translator = str.maketrans(punctuation_and_numbers, " " * len(punctuation_and_numbers))
#     word = word.translate(translator)
#     word = word.strip()
#     return word

def preprocess_word(word):
    # print("Original:", word)
    word = word.lower()
    word = word.replace("'", "") 
    if "(" in word or ")" in word:
        # print("Original:", word)
        word = word.replace("(", "").replace(")", "")
        # print("Processed:", word)
        word = word.strip()
        if not word: return " "
    for char in punctuation_and_numbers:
        word = word.replace(char, " ")
    word = word.strip()  
    # print("Processed:", word)
    return word

def word_frequencies(filename):
    d = {}  # crate empty dictionary    
    # load file
    with open(filename, 'r') as file:
        for line in file:
            words = line.split()        # read each word
            # print(words)
            if words:
                for word in words:
                    # Split hyphenated words
                    # print("Original word: ", word)
                    if "-" in word or "—" in word:
                        subwords = word.split("-")
                        subwords = [subword.split("—") for subword in subwords]
                        subwords = [item for subitem in subwords for item in subitem]
                        for subword in subwords:
                            processed_subword = preprocess_word(subword)  # Process each 
                            # print("Processed word: ", processed_subword)
                            if processed_subword and processed_subword.strip() != "":
                                if processed_subword in d:           # if word is already in the dictionary increment count
                                    d[processed_subword] += 1   
                                else:               # if word not in dictionary, add it and set count to 1
                                    d[processed_subword] = 1
                    else:
                        word = preprocess_word(word)
                        # print("Processed word: ", word)
                        if word and word.strip() != "":
                            if word in d:           # if word is already in the dictionary increment count
                                d[word] += 1   
                            else:               # if word not in dictionary, add it and set count to 1
                                d[word] = 1
    # print(d)
    return d

def print_map_by_value(map):
    for k, v in sorted(map.items(), key=itemgetter(1), reverse=True):
        print("%6d %s" % (v, k) )


def main():
    # files = ["pytest", "turing", "austen"]   # only use this if you are working on the optional austen challenge, and uncomment test_austen() in frequency_test.py
    files = ["pytest", "turing"]             # use this one to pass frequency_test.py for project 3 completion
    # files = ["turing"]
    # files = ["pytest"]                         # once this works, try the others!
    for f in files:
        print("=" * 10, f, "=" * 10)
        print_map_by_value(word_frequencies("files/"+f+".txt"))

# Don't run main on import
if __name__ == "__main__":
    main()
