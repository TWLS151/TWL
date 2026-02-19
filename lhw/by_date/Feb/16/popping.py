# SWEA - 1868
# 파핑파핑 지뢰찾기

import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10 ** 7)

# 8방향에 지뢰가 없는 칸은 연쇄를 일으킨다.

dirs = [
    (-1, 0), (1, 0), (0, -1), (0, 1),
    (-1, -1), (-1, 1), (1, -1), (1, 1)
]  # 8방향

# 일단 8 방향 탐색하는 for문
# count = 0
# for dr, dc in dirs:
#     nr, nc = r + dr, c + dc
#     if field[nr][nc] != 0:
#         count += 1

# DFS 를 쓰고 싶은데 N이 300이네..

# 0으로 이루어진 땅 개수 찾고 지뢰 아닌 숫자 개수 새면 되긴 하는데
# 안터질거 같기도 하고?

def dfs(r, c):
    for dr, dc in dirs:
        nr, nc = r+dr, c+dc
        if 0<=nr<N and 0<=nc<N and mines[nr][nc] in '.' and not visited[nr][nc]:
            visited[nr][nc] = True
            dfs(nr, nc)
        elif 0<=nr<N and 0<=nc<N and mines[nr][nc] == '1' and not visited[nr][nc]:
            visited[nr][nc] = True
    pass

TC = int(input())
for test_case in range(1, TC+1):
    N = int(input())
    mines = [[i for i in input()] for _ in range(N)]
    visited = [[False]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if mines[i][j] == '*':
                for dr, dc in dirs:
                    nr, nc = i+dr, j+dc
                    if 0<=nr<N and 0<=nc<N and mines[nr][nc] == '.':
                        mines[nr][nc] = '1'
    # 지뢰 주변은 다 1이 되었다.
    # 이제 .으로 이루어진 섬의 개수를 찾으면 됨

    # 지뢰를 찾아서 들어가야겠따.
    # 지뢰에서 진입하고 지뢰 주변에 지뢰가 아닌게 있으면 숫자 할당
    count = 0
    for i in range(N):
        for j in range(N):
            if mines[i][j] == '.' and not visited[i][j]:
                visited[i][j] = True
                dfs(i, j)
                count += 1
    
    for i in range(N):
        for j in range(N):
            if mines[i][j] == '1' and not visited[i][j]:
                count += 1

    print(f'#{test_case} {count}')