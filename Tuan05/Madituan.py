n, x0, y0 = map(int, input().split())

board = [[0]*n for _ in range(n)]

dx = [-2,-2,-1,-1,1,1,2,2]
dy = [-1,1,-2,2,-2,2,-1,1]

board[x0][y0] = 1
found = False


def inside(x,y):
    return 0 <= x < n and 0 <= y < n and board[x][y] == 0


def printBoard():
    print(1)
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()


def Try(x,y,step):
    global found

    if step == n*n:
        printBoard()
        found = True
        return

    for i in range(8):

        nx = x + dx[i]
        ny = y + dy[i]

        if inside(nx,ny):

            board[nx][ny] = step + 1

            Try(nx,ny,step+1)

            if found:
                return

            board[nx][ny] = 0


Try(x0,y0,1)

if not found:
    print(0)