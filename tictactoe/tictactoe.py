"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # Count the number of empty squares in the provided board
    num_empty = 0
    for row in board:
        for cell in row:
            if cell == EMPTY:
                num_empty += 1
    # If there are an odd number of empty squares, then it must be player 1's turn
    if num_empty % 2:
        return X
    return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
     # Add any empty square to the actions set
    action_set = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                action_set.add((i, j))
    return action_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    curr_board = deepcopy(board)
    # Raise an exception if the action is tried on a square that is non-empty
    if (curr_board[action[0]][action[1]] != EMPTY):
        raise TypeError("Invalid Action")
    # Update the temporary board with the result of the action
    elif (player(board) == X):
        curr_board[action[0]][action[1]] = X
    else:
        curr_board[action[0]][action[1]] = O
    return curr_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    for row in board:
        if (row == [X, X, X]):
            return X
        elif (row == [O, O, O]):
            return O
    # Check columns
    for i in range(len(board)):
        if (board[0][i] == board[1][i] == board[2][i] == X):
            return X
        elif (board[0][i] == board[1][i] == board[2][i] == O):
            return O

    # Check diagonals
    if (board[0][0] == board[1][1] == board[2][2] == X or board[0][2] == board[1][1] == board[2][0] == X):
        return X
    elif (board[0][0] == board[1][1] == board[2][2] == O or board[0][2] == board[1][1] == board[2][0] == O):
        return O

    return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    for row in board:
        for element in row:
            if element == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if (winner(board) == X):
        return 1
    elif (winner(board) == O):
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    optimal_move = None
    # Return None if the current board state is terminal
    if terminal(board):
        return optimal_move
    # Maximize the set of minimized moves if the current move is X
    if player(board) == X:
        _max = -2
        for action in actions(board):
            min_val = min_value(result(board, action))
            if  min_val > _max:
                _max = min_val
                optimal_move = action
        return optimal_move
    else:
        _min = 2
        for action in actions(board):
            max_val = max_value(result(board, action))
            if max_val < _min:
                _min = max_val
                optimal_move = action
        return optimal_move

def max_value(board):
    if terminal(board):
        return utility(board)
    max_val = -2
    for action in actions(board):
        max_val = max(max_val, min_value(result(board, action)))
    return max_val

def min_value(board):
    if terminal(board):
        return utility(board)
    min_val = 2
    for action in actions(board):
        min_val = min(min_val, max_value(result(board, action)))
    return min_val
