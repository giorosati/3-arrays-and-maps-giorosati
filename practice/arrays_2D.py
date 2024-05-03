# PREDICT ME!
# What do you think is output by this program?

def print_2D(b):
    for i in range(len(b)):
        print("[", end=" ")
        for j in b[i]:
            print(j, end=" ")
        print("]")


def main():
    boards = [ [ ["O", "X", "O"] ] * 3, \
               [ ['O', 'O', 'X'], ['O', 'X', 'O'], ['X', 'O', 'O'] ], \
               [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ], \
               [ [i for i in range(1,4)] ] * 3, \
               [ [i for i in range(1, 4)], [i for i in range(4, 7)], [i for i in range(7, 10)] ]
              ]
    for b in boards:
        print_2D(b)
        print("=" * 10)


# Don't run main on import
if __name__ == "__main__":
    main()

# OUTPUT
# [ O X O ]
# [ O X O ]
# [ O X O ]
# ==========
# [ O O X ]
# [ O X O ]
# [ X O O ]
# ==========
# [ 1 2 3 ]
# [ 4 5 6 ]
# [ 7 8 9 ]
# ==========
# [ 1 2 3 ]
# [ 1 2 3 ]
# [ 1 2 3 ]
# ==========
# [ 1 2 3 ]
# [ 4 5 6 ]
# [ 7 8 9 ]
# ==========
