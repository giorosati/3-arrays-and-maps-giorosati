# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 3: DID I WIN TIC-TAC-TOE?
#
# NAME:         Giovanni Rosati
# ASSIGNMENT:   Project 3: Arrays & Maps

# takes a player character and a 2-dimensional
# array as parameters and returns whether the
# player won the game
# HINT: What does a boolean accumulator look like?
def did_I_win_2D(player, board):
    # check that rows and columns are both = 3
    if len(board) != 3: return False
    if len(board[1]) != 3: return False

    did_win = True
    
    # check for player in all columns of each row
    for column in range(3):
        did_win = True
        for row in range(3):
            did_win &= player == board[row][column]
        if did_win == True: 
            return did_win
    
    # check for player in all rows of each column
    for row in range(3):
        did_win = True
        for column in range(3):
            did_win &= player == board[row][column]
        if did_win == True:
            return did_win

    # check for player on down-to-right diagonal
    did_win = True
    for i in range(3):
        did_win &= player == board[i][i]
    if did_win == True: 
        return did_win

    # check for player on up-to-right diagonal
    sequence = [[0,2],[1,1],[2,0]]
    did_win = True
    for pair in sequence:
        did_win &= player == board [pair[0]][pair[1]]
    if did_win == True:
        return did_win
    
    # if did_win never becomes True
    return did_win


def print_2D_board(b):
    for i in range(len(b)):
        print(b[i])

def main():
    boards = [ [["X", "O", "O"]] * 3, \
               [["X", "O", "X"], ["O"] * 3, ["O", "X", "O"]], \
               [['O', 'O', 'X'], ['O', 'X', 'O'], ['X', 'O', 'O']], \
               [["O", "O", "X"]] * 3 ]
    for b in boards:
        print_2D_board(b)
        print("X won?", did_I_win_2D("X", b))
        print("O won?", did_I_win_2D("O", b))

# Don't run main on import
if __name__ == "__main__":
    main()
