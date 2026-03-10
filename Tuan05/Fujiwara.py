# Nhập bảng Sudoku
board = []
for _ in range(9):
    row = list(input().strip())
    board.append(row)


# Kiểm tra hợp lệ
def valid(r, c, num):

    num = str(num)

    # kiểm tra hàng
    for i in range(9):
        if board[r][i] == num:
            return False

    # kiểm tra cột
    for i in range(9):
        if board[i][c] == num:
            return False

    # kiểm tra ô 3x3
    sr = (r//3)*3
    sc = (c//3)*3

    for i in range(3):
        for j in range(3):
            if board[sr+i][sc+j] == num:
                return False

    return True


# tìm ô trống
def findEmpty():

    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                return i, j

    return None


# Backtracking
def solve():

    pos = findEmpty()

    if not pos:
        return True

    r, c = pos

    for num in range(1, 10):

        if valid(r, c, num):

            board[r][c] = str(num)

            if solve():
                return True

            board[r][c] = '.'

    return False


# Chạy chương trình
if solve():

    for row in board:
        print("".join(row))

else:
    print("IMPOSSIBLE")