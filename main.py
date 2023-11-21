# AI powered tic-tac-toe game
import os

from minimax import best_move
from constants import AI, board_array
from helpers import check_winner


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


def start_game():
    playing = True
    move_result = None
    best_move(board_array)
    while playing:
        draw_board(board_array)
        index = input()
        insert_value(board_array, tuple(int(i) for i in str(index)))
        best_move(board_array)

        move_result = check_winner(board_array)
        if move_result is not None:
            playing = False
            draw_board(board_array)

    if move_result == 'tie':
        print('game ended with tie')
    else:
        print(f'played {move_result} has won')


start_game()
