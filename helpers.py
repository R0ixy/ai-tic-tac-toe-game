import os


def check_winner(board: list[list]):
    """Checks if state s is a terminal state"""

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


def player(board: list):
    """Returns which player to move"""

    x_number = 0
    o_number = 0
    for row in board:
        x_number += row.count('X')
        o_number += row.count('O')
    return 0 if x_number > o_number else 1


def draw_board(spots):
    """Draws a board"""

    os.system('cls' if os.name == 'nt' else 'clear')

    board = f' 1 2 3 \n'

    for i, rows in enumerate(spots):
        board += f'{i + 1}|'
        for elements in rows:
            board += f'{elements}|'
        board += '\n'
    print(board)


def insert_value(spots: list, index: tuple[int]):
    """Inserts a value to the board"""

    if spots[index[0] - 1][index[1] - 1] == ' ':
        spots[index[0] - 1][index[1] - 1] = 'X' if player(spots) == 1 else 'O'
    else:
        print('try again\n')
