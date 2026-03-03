# SWEA - 1226
# 미로1

import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt')

dirs = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]

def dfs(r, c):
    global er, ec, visited, field, can
    
    # 종료
    if (r, c) == (er, ec):
        can = 1
        return
    
    if can == 1:
        return

    # 내용
    for dr, dc in dirs:
        nr, nc = r+dr, c+dc

        if not visited[nr][nc] and field[nr][nc] != 1:
            visited[nr][nc] = True
            dfs(nr, nc)
            visited[nr][nc] = False


for _ in range(10):
    test_case = int(input())
    N = 100
    field = []
    start = end = None
    for idx in range(N):
        row = list(map(int, list(input())))
        if not (start and end):
            for col in range(N):
                if row[col] == 2:
                    (sr, sc) = (idx, col)
                if row[col] == 3:
                    (er, ec) = (idx, col)
        field.append(row)
            
    visited = [[False] * N for _ in range(N)]

    visited[sr][sc] = True
    can = 0
    dfs(sr, sc)
    print(f"#{test_case} {can}")