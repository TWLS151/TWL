# BOJ - 2206
# 벽 부수고 이동하기

import sys
from collections import deque

sys.stdin = open('input.txt')

dirs = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]

def bfs(r, c, b):
    global N, M, field

    q = deque()
    dist = [[[0]*2 for _ in range(M)] for _ in range(N)]

    q.append((r, c, b))
    dist[r][c][b] = 1

    while q:
        r, c, b = q.popleft()

        if r == N-1 and c == M-1:
            return dist[r][c][b]

        for dr, dc in dirs:
            nr, nc = r+dr, c+dc

            if 0 <= nr < N and 0 <= nc < M:
                if field[nr][nc] == 0 and dist[nr][nc][b] == 0:
                        q.append((nr, nc, b))
                        dist[nr][nc][b] = dist[r][c][b] + 1
                elif field[nr][nc] == 1 and b == 0 and dist[nr][nc][1] == 0:
                    q.append((nr, nc, 1))
                    dist[nr][nc][1] = dist[r][c][b] + 1
    return -1



N, M, K = map(int, input().split())
field = [[int(i) for i in input()] for _ in range(N)]

print(bfs(0, 0, 0))