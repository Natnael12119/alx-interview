#!/usr/bin/python3
import sys

def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at board[row][col].
    This means checking the column and both diagonals.
    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(n):
    """
    Solve the N Queens problem and print all solutions.
    """
    def backtrack(row=0):
        if row == n:
            solution = [[i, board[i]] for i in range(n)]
            solutions.append(solution)
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1)
    
    board = [-1] * n
    solutions = []
    backtrack()
    return solutions

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(n)
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    main()
