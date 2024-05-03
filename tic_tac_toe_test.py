from tic_tac_toe import did_I_win_2D

def test_3_3_X():
    b = [ ["X"] * 3 ] * 3
    assert did_I_win_2D("X", b) == True

def test_3_3_O():
    b = [ ["X"] * 3 ] * 3
    assert did_I_win_2D("O", b) == False

def test_1_2d_X():
    b = [["X", "O", "O"]] * 3
    assert did_I_win_2D("X", b) == True

def test_1_2_O():
    b = [["X", "O", "O"]] * 3
    assert did_I_win_2D("O", b) == True

def test_1_2_V():
    b = [["X", "X", "X"]] * 3
    assert did_I_win_2D("V", b) == False

def test_1_O_X():
    b = [["X", "O", "X"], ["O"] * 3, ["O", "X", "O"]]
    assert did_I_win_2D("X", b) == False

def test_1_O_O():
    b = [["X", "O", "X"], ["O"] * 3, ["O", "X", "O"]]
    assert did_I_win_2D("O", b) == True

def test_1_d_X():
    b = [['O', 'O', 'X'], ['O', 'X', 'O'], ['X', 'O', 'O']]
    assert did_I_win_2D("X", b) == True

def test_1_d_O():
    b = [['O', 'O', 'X'], ['O', 'X', 'O'], ['X', 'O', 'O']]
    assert did_I_win_2D("O", b) == False

def test_3_d_X():
    b = [['X', 'O', 'O'], ['O', 'X', 'O'], ['O', 'O', 'X']]
    assert did_I_win_2D("X", b) == True

def test_3_a1_X():
    b = [['X'] * 3, ["O"] * 3, ["O"] * 3]
    assert did_I_win_2D("X", b) == True

def test_3_a2_X():
    b = [["O"] * 3, ['X'] * 3, ["O"] * 3]
    assert did_I_win_2D("X", b) == True

def test_3_a3_X():
    b = [["O"] * 3, ["O"] * 3, ['X'] * 3]
    assert did_I_win_2D("X", b) == True

def test_3_2d_O():
    b = [["O", "O", "X"]] * 3
    assert did_I_win_2D("X", b) == True

def test_3_1d_O():
    b = [["O", "X", "O"]] * 3
    assert did_I_win_2D("X", b) == True

def test_0():
    b = []
    assert did_I_win_2D("X", b) == False

def test_1():
    b = [["X"]] * 3
    assert did_I_win_2D("X", b) == False

def test_2():
    b = [ ["X"] * 3 ] * 2
    assert did_I_win_2D("X", b) == False

def test_4():
    b = [ ["X"] * 4 ] * 3
    assert did_I_win_2D("X", b) == False

def test_10():
    b = [ ["X"] * 10 ] * 10
    assert did_I_win_2D("X", b) == False