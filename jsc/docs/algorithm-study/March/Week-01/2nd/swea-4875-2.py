import sys
from collections import deque
sys.stdin = open('swea-4875.txt')

dr = [-1, 1, 0, 0, -1, -1, 1, 1]
dc = [0, 0, -1, 1, -1, 1, -1, 1]

def flip(r, c, d, color, path, board):
    nr, nc = r + dr[d], c + dc[d]

    if (0 <= nr < N and 0 <= nc < N) or board[nr][nc] == 0:
        return False
    
    if board[nr][nc] == color:
        if path:
            return True
        else:
            return False
        
    if board[nr][nc] != color:
        path.append(board[nr][nc])
        if flip(nr, nc, d, color, path, board):
            return True
        else:
            return False



                
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    result = 0

    # 시작점(2) 찾기
    start_r, start_c = -1, -1
    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                start_r, start_c = i, j
                break

    # DFS 시작
    dfs(start_r, start_c)

    print(f'#{tc} {result}')

    