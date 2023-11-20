# AI powered tic-tac-toe game
import os

from minimax import minimax
from constants import AI, board_array
from helpers import check_winner


def player(board: list):
    # returns which player to move in state s
    x_number = 0
    o_number = 0
    for row in board:
        x_number += row.count('X')
        o_number += row.count('O')
    return 0 if x_number > o_number else 1


def draw_board(spots):
    os.system('cls' if os.name == 'nt' else 'clear')

    board = f' 1 2 3 \n'

    for i, rows in enumerate(spots):
        board += f'{i + 1}|'
        for elements in rows:
            board += f'{elements}|'
        board += '\n'
    print(board)


def insert_value(spots: list, index: tuple[int]):
    if spots[index[0] - 1][index[1] - 1] == ' ':
        spots[index[0] - 1][index[1] - 1] = 'X' if player(spots) == 1 else 'O'
    else:
        print('try again\n')


def best_move(board):
    best_score = float('-inf')
    move = ()
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = AI
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)

    board[move[0]][move[1]] = AI


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
