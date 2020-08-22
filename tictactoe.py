"""
Tic Tac Toe Player
"""

import math
import random
import numpy as np
import copy
import sys


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


def Player(board):
    """
    Returns player who has the next turn on a board.
    """
    if board == initial_state():
        return X

    nparrayboard = np.array(board)
    Xcount = np.count_nonzero(nparrayboard == X)
    Ocount = np.count_nonzero(nparrayboard == O)

    if Xcount > Ocount:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actionset = set()
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] == EMPTY:
                actionset.add((i, j))

    return actionset


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    i = action[0]
    j = action[1]

    if board[i][j] != EMPTY:
        raise Exception('Invalid action')

    oppositeplayer = Player(board)
    newBoard = copy.deepcopy(board)
    newBoard[i][j] = oppositeplayer
    return newBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if row[0] != EMPTY and row[0] == row[1] == row[2]:
            return row[0]

    for col in range(len(board)):
        if board[0][col] != EMPTY and board[0][col] == board[1][col] == board[2][col]:
            return board[0][col]
    # main diagonal
    if board[0][0] != EMPTY and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    # 2nd diagonal
    if board[0][2] != EMPTY and board[0][2] == board[2][0] == board[1][1]:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
         return True

    numpyBoard = np.array(board)
    count = np.count_nonzero(numpyBoard == EMPTY)
    if count == 0:
        return True

    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    gw = winner(board)
    if gw == X:
        return 1

    if gw == O:
        return -1

    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    cp = Player(board)
    if cp == X:
        return Maximum(board)[1]
    else:
        return Minimum(board)[1]

def Maximum(board):
    if terminal(board):
        return (utility(board), None)

    val = -sys.maxsize-1
    nextaction = None

    al = list(actions(board))
    random.shuffle(al)

    for action in al:
        res = Minimum(result(board, action))
        if res[0] > val:
            val = res[0]
            nextaction = action

        if val == 1:
            break

    return (val, nextaction)


def Minimum(board):
    if terminal(board):
        return (utility(board), None)

    val = sys.maxsize
    nextaction = None

    al = list(actions(board))
    random.shuffle(al)

    for action in al:
        res = Maximum(result(board, action))
        if res[0] < val:
            val = res[0]
            nextaction = action

        if val == -1:
            break

    return (val, nextaction)