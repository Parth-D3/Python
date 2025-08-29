## BACKTRACKKING WITH DFS ##

def print_board(board):
    for r in range(9):
        if r % 3 == 0 and r != 0:
            print("-" * 21)
        for c in range(9):
            if c % 3 == 0 and c != 0:
                print("|", end=" ")
            print(board[r][c] if board[r][c] != 0 else ".", end=" ")
        print()

def is_valid(board, row, col, num):
    # check row
    if num in board[row]:
        return False
    
    # check col
    if num in [board[r][col] for r in range(9)]:
        return False
    
    # check 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if board[r][c] == num:
                return False
    return True

def find_empty(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return r, c
    return None

count = 0
def solve(board):
    global count
    count+=1
    empty = find_empty(board)  #check for 0 or -1 for empty cell
    if not empty:
        return True  # solved
    
    row, col = empty
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve(board):
                return True
            board[row][col] = 0
    return False

# Example Sudoku puzzle (0 = empty)
sudoku_board = [
    [5,3,0, 0,7,0, 0,0,0],
    [6,0,0, 1,9,5, 0,0,0],
    [0,9,8, 0,0,0, 0,6,0],
    
    [8,0,0, 0,6,0, 0,0,3],
    [4,0,0, 8,0,3, 0,0,1],
    [7,0,0, 0,2,0, 0,0,6],
    
    [0,6,0, 0,0,0, 2,8,0],
    [0,0,0, 4,1,9, 0,0,5],
    [0,0,0, 0,8,0, 0,7,9]
]

print("Sudoku Puzzle:")
print_board(sudoku_board)

if solve(sudoku_board):
    print("\nSolved Sudoku:")
    print_board(sudoku_board)
else:
    print("No solution exists")

print(count)
