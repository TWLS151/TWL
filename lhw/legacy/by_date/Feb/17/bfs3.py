# BOJ - 1600
# 말이 되고픈 원숭이

# import sys
from collections import deque

# sys.stdin = open('input.txt')

dirs = [
    (-1, 0), (1, 0), (0, -1), (0, 1),
]

horse = [
    (2, 1), (1, 2), (2, -1), (1, -2),
    (-1, -2), (-2, -1), (-2, 1), (-1, 2)
]

def bfs():

    q = deque()
    dist = [[[-1]*(K+1) for _ in range(W)] for _ in range(H)]

    q.append((0, 0, 0))
    dist[0][0][0] = 0

    while q:
        r, c, s = q.popleft()

        if (r, c) == (H-1, W-1):
            return dist[r][c][s]

        for dr, dc in dirs:
            nr, nc = r+dr, c+dc
            if 0 <= nr < H and 0 <= nc < W:
                if field[nr][nc] == 0 and dist[nr][nc][s] == -1:
                    q.append((nr, nc, s))
                    dist[nr][nc][s] = dist[r][c][s] + 1

        if s < K:
            for dr, dc in horse:
                nr, nc = r+dr, c+dc
                if 0 <= nr < H and 0 <= nc < W:
                    if field[nr][nc] == 0 and dist[nr][nc][s+1] == -1:
                        q.append((nr, nc, s+1))
                        dist[nr][nc][s+1] = dist[r][c][s] + 1

    return -1


K = int(input())
W, H = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(H)]


# r, c, 말처럼 이동 횟수
print(bfs())
