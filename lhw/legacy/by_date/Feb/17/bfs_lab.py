# BOJ - 14502
# 연구소

import sys
sys.stdin = open('input.txt')

from collections import deque
from itertools import combinations

N, M = map(int, input().split())
labo = [list(map(int, input().split())) for _ in range(N)]

dirs = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]

def bfs(lst):
    dist = [[0]*M for _ in range(N)]

    for r, c in lst:
        q = deque([(r, c)])
        dist[r][c] = 1

        while q:
            pr, pc = q.popleft()
            for dr, dc in dirs:
                nr, nc = pr+dr, pc+dc
                if 0<=nr<N and 0<=nc<M and dist[nr][nc]==0 and labo[nr][nc]==0:
                    q.append((nr, nc))
                    dist[nr][nc] = dist[r][c] + 1
    
    count = 0
    for i in range(N):
        for j in range(M):
            if labo[i][j] == 0 and dist[i][j] == 0:
                count += 1
    return count


empty = []
walls = []
virus = []
for i in range(N):
    for j in range(M):
        if labo[i][j] == 0:
            empty.append((i, j))
        if labo[i][j] == 1:
            walls.append((i, j))
        if labo[i][j] == 2:
            virus.append((i, j))

new_walls = combinations(empty, 3)

max_result = 0
for wall in new_walls:
    for r, c in wall:
        labo[r][c] = 1

    result = bfs(virus)
    if result > max_result:
        max_result = result

    for r, c in wall:
        labo[r][c] = 0

print(max_result)