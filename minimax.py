from constants import SCORES, AI, HUMAN
from helpers import check_winner


def best_move(board):
    best_score = float('-inf')
    move = ()
    for i, row in enumerate(board):
        for j, element in enumerate(row):
            if element == ' ':
                board[i][j] = AI
                score = minimax(board, 0, float('-inf'), float('inf'), False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)

    board[move[0]][move[1]] = AI


def minimax(board, depth, alpha, beta, is_maximizing):
    move_result = check_winner(board)

    if move_result is not None:
        return SCORES[move_result]

    if is_maximizing:
        best_score = float('-inf')
        for i, row in enumerate(board):
            for j, element in enumerate(row):
                if element == ' ':
                    board[i][j] = AI
                    score = minimax(board, depth + 1, alpha, beta, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
                    alpha = max(alpha, score)
                    if beta <= alpha:
                        break
        return best_score
    else:
        best_score = float('inf')
        for i, row in enumerate(board):
            for j, element in enumerate(row):
                if element == ' ':
                    board[i][j] = HUMAN
                    score = minimax(board, depth + 1, alpha, beta, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
                    beta = min(beta, score)
                    if beta <= alpha:
                        break
        return best_score
