#!/usr/bin/env python3

import sys


with open("day4.input", "r") as file:
    data = file.read().strip().split("\n\n")

numbers, boards = data[0], data[1:]
numbers = numbers.split(',')


def map_board(board):
    split = board.split("\n")
    return {
        complex(x, y): [num, False]
        for y, row in enumerate(split)
        for x, num in enumerate(row.split())
    }


def check_board_state(board, num):
    rows = [(0j, 1+0j, 2+0j, 3+0j, 4+0j),
            (1j, 1+1j, 2+1j, 3+1j, 4+1j),
            (2j, 1+2j, 2+2j, 3+2j, 4+2j),
            (3j, 1+3j, 2+3j, 3+3j, 4+3j),
            (4j, 1+4j, 2+4j, 3+4j, 4+4j)]

    cols = [(0+0j, 0+1j, 0+2j, 0+3j, 0+4j),
            (1+0j, 1+1j, 1+2j, 1+3j, 1+4j),
            (2+0j, 2+1j, 2+2j, 2+3j, 2+4j),
            (3+0j, 3+1j, 3+2j, 3+3j, 3+4j),
            (4+0j, 4+1j, 4+2j, 4+3j, 4+4j)]

    for row in rows:
        row_state = [board[idx][1] for idx in row]
        if False in row_state:
            continue
        else:
            calculate_score(board, num)
            sys.exit()

    for col in cols:
        col_state = [board[idx][1] for idx in col]
        if False in col_state:
            continue
        else:
            calculate_score(board, num)
            sys.exit()


def calculate_score(board, num):
    unmarked = [int(i[0]) for i in board.values() if i[1] is False]
    print(sum(unmarked)*int(num))


def solve_boards(boards):
    for idx, num in enumerate(numbers):
        for board in boards:
            board_values = list(board.values())
            for spot in board_values:
                if num == spot[0]:
                    spot[1] = True
                    if idx > 3:
                        check_board_state(board, num)


mapped_boards = [map_board(board) for board in boards]
solve_boards(mapped_boards)
