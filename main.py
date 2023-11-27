# AI powered tic-tac-toe game

from minimax import best_move
from constants import AI, board_array
from helpers import check_winner, draw_board, insert_value


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


if __name__ == '__main__':
    start_game()

