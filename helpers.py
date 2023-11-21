def check_winner(board: list[list]):
    """checks if state s is a terminal state"""

    winner = None

    # horizontal
    for i in range(3):
        if equals(board[i][0], board[i][1], board[i][2]):
            winner = board[i][0]

    # vertical
    for i in range(3):
        if equals(board[0][i], board[1][i], board[2][i]):
            winner = board[0][i]

    # diagonal
    if equals(board[0][0], board[1][1], board[2][2]):
        winner = board[0][0]
    if equals(board[2][0], board[1][1], board[0][2]):
        winner = board[2][0]

    open_slots = 0
    for rows in board:
        open_slots += rows.count(' ')

    if winner is None and open_slots == 0:
        return 'tie'
    else:
        return winner


def equals(a, b, c):
    """Checks if a, b, c are equal"""
    return a == b and b == c and a != ' '
