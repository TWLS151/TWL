import sys

sys.stdin = open('swea-4875.txt')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c, N):
    if board[r][c] == 3:
        return True

    board[r][c] = 1

    for dir in range(4):
        nr, nc = r + dr[dir], c + dc[dir]
        
        if 0 <= nr < N and 0 <= nc < N and board[nr][nc] !=1:
            if dfs(nr, nc, N):
                return True
    
    return False
    pass



T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                start_r, start_c = i, j

    if dfs(start_r, start_c, N):
        print('1')
    else:
        print('0')
        pass