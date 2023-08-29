from tictactoe import EMPTY, X, O, player, actions, result, terminal, winner

def test_player():
    assert(player([[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]) == X)
    assert(player([[X, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]) == O)
    assert(player([[X, EMPTY, EMPTY],
            [EMPTY, O, O],
            [EMPTY, EMPTY, X]]) == X)


def test_actions():
    assert(actions([[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]) == {(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)})

def test_result():
    assert(result([[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]], (0, 0)) == [[X, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]])

def test_winner():
    assert(winner([[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]) == None)
    assert(winner([[X, EMPTY, EMPTY],
            [EMPTY, X, EMPTY],
            [EMPTY, EMPTY, X]]) == X)
    assert(winner([[O, O, O],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]) == O)
    assert(winner([[X, O, O],
            [X, EMPTY, EMPTY],
            [X, EMPTY, EMPTY]]) == X)
    assert(winner([[O, X, O],
            [O, EMPTY, EMPTY],
            [O, EMPTY, EMPTY]]) == O)

def test_terminal():
    assert(terminal([[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]) == False)
    assert(terminal([[X, EMPTY, EMPTY],
            [EMPTY, X, EMPTY],
            [EMPTY, EMPTY, X]]) == True)
    assert(terminal([[O, O, O],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]) == True)
    assert(terminal([[X, O, O],
            [X, EMPTY, EMPTY],
            [X, EMPTY, EMPTY]]) == True)
    assert(terminal([[O, X, O],
            [O, EMPTY, EMPTY],
            [O, EMPTY, EMPTY]]) == True)
    assert(terminal([[O, X, O],
            [O, X, O],
            [X, O, X]]) == True)