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
def word_frequencies(filename):
    d = {}  # crate empty dictionary
    punctuation_and_numbers = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~0123456789"
    # spaces = len(punctuation_and_numbers)
    # spaces_string = ""
    # for i in range(spaces):
    #     spaces_string = spaces_string + " "

    # replacement_table = str.maketrans('', spaces_string, punctuation_and_numbers)
    
    # load file
    with open(filename, 'r') as file:
        for line in file:
            words = line.split()        # read each word
            for word in words:
                word = word.lower()     # make all letters lowercase
                word.replace("'", "")   # remove apostrophes
                for character in punctuation_and_numbers:
                    word = word.replace(character, " ")
                # word = word.translate(replacement_table) # replace punctuation and numbers with a space
                if word in d:           # if word is already in the dictionary increment count
                    d[word] += 1   
                else:               # if word not in dictionary, add it and set count to 1
                    d[word] = 1
    return d

def print_map_by_value(map):
    for k, v in sorted(map.items(), key=itemgetter(1), reverse=True):
        print("%6d %s" % (v, k) )


def main():
    # files = ["pytest", "turing", "austen"]   # only use this if you are working on the optional austen challenge, and uncomment test_austen() in frequency_test.py
    # files = ["pytest", "turing"]             # use this one to pass frequency_test.py for project 3 completion
    files = ["pytest"]                         # once this works, try the others!
    for f in files:
        print("=" * 10, f, "=" * 10)
        print_map_by_value(word_frequencies("files/"+f+".txt"))

# Don't run main on import
if __name__ == "__main__":
    main()
