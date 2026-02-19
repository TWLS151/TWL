# BOJ - 14442
# 벽 부수고 이동하기 2

# 시간초과.
# 일단 테스트케이스는 모두 통과, AI도 큰 문제 없다는 판단.
# dist가 int 3차원이라 많이 무겁다고 하는데 나중에 최적화해보자

import sys
from collections import deque

# sys.stdin = open('input.txt')


dirs = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]

def bfs():
    q = deque()
    dist = [[[0]*(K+1) for _ in range(M)] for _ in range(N)]

    q.append((0, 0, 0))
    dist[0][0][0] = 1

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

                elif field[nr][nc] == 1 and b < K and dist[nr][nc][b+1] == 0:
                    q.append((nr, nc, b+1))
                    dist[nr][nc][b+1] = dist[r][c][b] + 1

    return -1

N, M, K = map(int, input().split())
field = [[int(i) for i in input()] for _ in range(N)]

print(bfs())