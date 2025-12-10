import os
import time

# -------------------------------
# Board setup
# -------------------------------
board = [["-" for _ in range(9)] for _ in range(9)]

# Add row numbers and column letters
for i, letter in enumerate("ABCDEFGH"):
    board[i][8] = str(8 - i)
    board[8][i] = letter

# -------------------------------
# Queen positions
# -------------------------------
queens = []

# Ask for initial queen position
initial_pos = input("\033[32mEnter the initial position of the first queen (e.g., A7, C2...): \033[m").upper()
queens.append(initial_pos)

# Place the first queen on the board
for i, letter in enumerate("ABCDEFGH"):
    if queens[0][0] == letter:
        row = 8 - int(queens[0][1])
        col = i
        board[row][col] = "\033[31mX\033[m"
        queens.append((row, col))
        queens.pop(0)

# Clear screen and print initial board
os.system('cls' if os.name == 'nt' else 'clear')
for row in board:
    print(" ".join(row))


# -------------------------------
# Functions
# -------------------------------
def can_place_queen(board, row, col, queens):
    """Check if a queen can be safely placed at (row, col)."""

    # Check row
    if "\033[31mX\033[m" in board[row]:
        return False

    # Check column
    for q in queens:
        if q[1] == col:
            return False

    # Check diagonals
    for q in queens:
        if abs(q[0] - row) == abs(q[1] - col):
            return False

    return True


def place_queens(board, queens):
    """Recursive backtracking function to place all queens."""
    if len(queens) < 8:
        for row in range(8):
            for col in range(8):
                if board[row][col] == "-" and can_place_queen(board, row, col, queens):
                    board[row][col] = "\033[31mX\033[m"
                    queens.append((row, col))

                    # Clear screen and display current board
                    os.system('cls' if os.name == 'nt' else 'clear')
                    for r in board:
                        print(" ".join(r))
                    time.sleep(0.5)  # Adjust speed

                    if place_queens(board, queens):
                        return True

                    # Backtrack
                    queens.pop()
                    board[row][col] = "-"
    else:
        return True


# -------------------------------
# Start algorithm
# -------------------------------
place_queens(board, queens)
