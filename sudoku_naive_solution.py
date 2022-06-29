# Naive sudoku solution using backtracking.

RED = "\033[31m"
NO_COLOR = "\033[0m"

def print_board(board, empty_cells):
    print()

    for r in range(9):
        for c in range(9):
            COL = NO_COLOR

            if [r, c] in empty_cells:
                COL = RED
            
            print("{0}{1}{2} ".format(COL, board[r][c], NO_COLOR), end="")

            if c % 3 == 2 and c != 8:
                print("| ", end="")
        
        print("")

        if r % 3 == 2 and r != 8:
            print("-" * 21)
    
    print()

def is_present_in_row(board, row, candidate):
    for num in board[row]:
        if num == candidate:
            return True
    
    return False

def is_present_in_column(board, column, candidate):
    for c in range(9):
        if board[c][column] == candidate:
            return True
    
    return False

def is_present_in_box(board, row, column, candidate):
    box_row = row // 3
    box_column = column // 3

    for r in range(box_row*3, box_row*3 + 3):
        for c in range(box_column*3, box_column*3 + 3):
            if board[r][c] == candidate:
                return True

    return False

def solve(board, empty_cells, index):
    if index == len(empty_cells):
        print_board(board, empty_cells)
        return

    row, column = empty_cells[index]

    for candidate in range(1, 10):
        if not is_present_in_row(board, row, candidate) and not is_present_in_column(board, column, candidate) and not is_present_in_box(board, row, column, candidate):
            board[row][column] = candidate
            solve(board, empty_cells, index+1)
            board[row][column] = 0
    

board = []

for cnt in range(9):
    row = [ int(i) for i in input().split() ]
    board.append(row)

empty_cells = []

for r in range(9):
    for c in range(9):
        if board[r][c] == 0:
            empty_cells.append([r, c])

solve(board, empty_cells, 0)