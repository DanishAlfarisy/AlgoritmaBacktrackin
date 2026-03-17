import time

board = [
[5,3,0,0,7,0,0,0,0],
[6,0,0,1,9,5,0,0,0],
[0,9,8,0,0,0,0,6,0],
[8,0,0,0,6,0,0,0,3],
[4,0,0,8,0,3,0,0,1],
[7,0,0,0,2,0,0,0,6],
[0,6,0,0,0,0,2,8,0],
[0,0,0,4,1,9,0,0,5],
[0,0,0,0,8,0,0,7,9]
]

def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")

            if board[i][j] == 0:
                print(".", end=" ")
            else:
                print(board[i][j], end=" ")

        print()
    print()


def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None


def valid(board, num, pos):
    row, col = pos

    # cek baris
    for j in range(9):
        if board[row][j] == num and j != col:
            return False

    # cek kolom
    for i in range(9):
        if board[i][col] == num and i != row:
            return False

    # cek grid 3x3
    box_x = col // 3
    box_y = row // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True


def solve(board):
    find = find_empty(board)

    if not find:
        return True

    row, col = find

    for num in range(1, 10):

        if valid(board, num, (row, col)):

            board[row][col] = num
            print_board(board)
            time.sleep(0.1)

            if solve(board):
                return True

            board[row][col] = 0
            print("Backtracking...")
            print_board(board)
            time.sleep(0.1)

    return False


print("Initial Sudoku:\n")
print_board(board)

solve(board)

print("Solved Sudoku:\n")
print_board(board)