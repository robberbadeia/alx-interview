#!/usr/bin/python3
"""
Function Implementation
"""


import sys


def print_usage_and_exit(message):
    print(message)
    sys.exit(1)


def is_valid(board, row, col):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_n_queens(n, board, row):
    if row == n:
        solution = [[i, board[i]] for i in range(n)]
        print(solution)
    else:
        for col in range(n):
            if is_valid(board, row, col):
                board[row] = col
                solve_n_queens(n, board, row + 1)
                board[row] = -1


def nqueens(n):
    if n < 4:
        print_usage_and_exit("N must be at least 4")
    board = [-1] * n
    solve_n_queens(n, board, 0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print_usage_and_exit("Usage: nqueens N")
    try:
        n = int(sys.argv[1])
    except ValueError:
        print_usage_and_exit("N must be a number")
    nqueens(n)
