"""
Tic Tac Toe Player
"""

import math
import copy

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
    numOfEmpty = 0
    for item in board:
      for i in item:
        if i == EMPTY:
          numOfEmpty += 1;
    if numOfEmpty % 2 == 0:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    options = set()
    for row in range(3):
        for column in range(3):
            if board[row][column] == EMPTY:
                options.add((row, column))
    return options



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    (row, column) = action
    cp = copy.deepcopy(board)
    cp[row][column] = player(board)
    return cp

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if row[0] == row[1] and row[1] == row[2]:
            return row[0]
    for column in range(3):
        if board[1][column] == board[0][column] and board[1][column] == board[2][column]:
            return board[1][column]
    if board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        return board[0][0]
    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[0][2]


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
      return winner(board)
      return False
    for item in board:
      for i in item:
        if i == EMPTY:
          return False
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    #check if game is over
    optimal = maximize(board)
    return optimal

def maximize (board):
    bestAction = None
    lastIteration = None
    bestScore = float("-inf")

    for action in actions(board):
        lastIteration = action
        maxResult = result(board, action)
        if terminal(maxResult) == True:
            score = utility(maxResult)
            if score > bestScore and action != None:
                bestScore = score
                bestAction = action
            if score == 1:
              return action
        else:
            minimize(maxResult)
    if bestAction == None:
      bestAction = lastIteration
    return bestAction        
    
            
        
def minimize (board):
    lastIteration = None
    bestAction = None
    bestScore = float("inf")

    for action in actions(board):
        lastIteration = action
        minResult = result(board, action)
        if terminal(minResult) == True:
            score = utility(minResult)
            if score < bestScore and action != None:
                bestScore = score
                bestAction = action
            if score == -1:
              return action
        else:
            maximize(minResult)
    if bestAction == None:
      bestAction = lastIteration
    return bestAction
