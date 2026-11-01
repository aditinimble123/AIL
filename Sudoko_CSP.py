# Sudoku Solver using Backtracking

board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


def print_board():
    for row in board:
        print(row)


def valid(num, row, col):

    for i in range(9):
        if board[row][i] == num:
            return False

        if board[i][col] == num:
            return False

    r = (row // 3) * 3
    c = (col // 3) * 3

    for i in range(r, r + 3):
        for j in range(c, c + 3):
            if board[i][j] == num:
                return False

    return True


def solve():

    for row in range(9):
        for col in range(9):

            if board[row][col] == 0:

                for num in range(1, 10):

                    if valid(num, row, col):

                        board[row][col] = num

                        if solve():
                            return True

                        board[row][col] = 0

                return False

    return True


print("Original Sudoku:")
print_board()

if solve():
    print("\nSolved Sudoku:")
    print_board()
else:
    print("No solution exists.")
    