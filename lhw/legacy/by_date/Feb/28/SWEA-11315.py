# SWEA - 11315
# 오목 판정

import sys
sys.stdin = open('input.txt')

dirs = [
    (1, 0), (0, 1), (1, -1), (1, 1)
]

def dfs(r, c, dr, dc, count):
    global N, board, result

    if count >= 5:
        result = 'YES'
        return
    
    nr, nc = r+dr, c+dc

    if 0 <= nr < N and 0 <= nc < N \
    and board[nr][nc] == 'o':
        dfs(nr, nc, dr, dc, count+1)

    pass

TC = int(input())
for test_case in range(1, TC+1):
    N = int(input())
    board = [input() for _ in range(N)]

    result = 'NO'
    for r in range(N):
        for c in range(N):
            if board[r][c] == 'o':
                for dr, dc in dirs:
                    dfs(r, c, dr, dc, 1)

    print(f"#{test_case} {result}")