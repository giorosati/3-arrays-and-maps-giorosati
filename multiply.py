# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 2: MULTIPLICATION TABLE
#
# NAME:         Giovanni Rosati
# ASSIGNMENT:   Project 3: Arrays & Maps

# Write a function called multiplication_table that
# takes a width, height, & scaling factor as parameters
# and returns a two-dimensional array multiplication
# table scaled by the scaling factor.
# You should not be using any functions other than range.
def multiplication_table(w, h, s):
    # populate values in column 0 and row 0
    return [ [ 0 for i in range(w)] for i in range(h)]

def print_2D(b):
    for i in range(len(b)):
        print(b[i])

def main():
    print("5 3 1:")
    print_2D(multiplication_table(5, 3, 1))
    print("5 3 2:")
    print_2D(multiplication_table(5, 3, 2))

# Don't run main on import
if __name__ == "__main__":
    main()

