# BOJ - 17142
# 연구소

import sys
# sys.stdin = open('input.txt')

from collections import deque
from itertools import combinations

dirs = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]

def bfs(lst):
    q = deque()
    dist = [[-1]*N for _ in range(N)]
    for r, c in lst:
        q.append((r, c))
        dist[r][c] = 0

    infected_empty = 0
    max_time = 0

    while q:
        r, c = q.popleft()

        for dr, dc in dirs:
            nr, nc = r+dr, c+dc

            if 0<=nr<N and 0<=nc<N:
                if dist[nr][nc] != -1:
                    continue
                if lab[nr][nc] == 1:
                    continue

                q.append((nr, nc))
                dist[nr][nc] = dist[r][c] + 1

                if lab[nr][nc] == 0:
                    infected_empty += 1
                    max_time = max(max_time, dist[nr][nc])

    if infected_empty != empty_cnt:
        return float('inf')
    return max_time


N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]


virus = []
empty_cnt = 0
for r in range(N):
    for c in range(N):
        if lab[r][c] == 2:
            virus.append((r, c))
        elif lab[r][c] == 0:
            empty_cnt += 1

if empty_cnt == 0:
    print(0)
    sys.exit()

cv = combinations(virus, M)
result = 2500
for v in cv:
    result = min(result, bfs(v))

print(-1 if result == float('inf') else result)