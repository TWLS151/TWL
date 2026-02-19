# SWEA - 4193
# 수영대회 결승전

import sys
from collections import deque
sys.stdin = open('input.txt')

dirs = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]

def bfs(sr, sc, t):
    global N, field, er, ec

    q = deque([(sr, sc, t)])
    dist = [[[-1]*3 for _ in range(N)] for _ in range(N)]
    dist[sr][sc][t] = 0
    # dist 를 시간으로 하면 되겠는데

    while q:

        r, c, t = q.popleft()

        nt = t + 1
        ntmod = nt % 3

        if (r, c) == (er, ec):
            return t

        if dist[r][c][ntmod] == -1:
            dist[r][c][ntmod] = nt
            q.append((r, c, nt))


        for dr, dc in dirs:
            nr, nc = r+dr, c+dc

            if 0 <= nr < N and 0 <= nc < N:
                if field[nr][nc] == 0:
                    q.append((nr, nc, nt))
                    dist[nr][nc][ntmod] = nt
                elif field[nr][nc] == 2:
                    if nt % 3 == 0:
                        if dist[nr][nc][ntmod] == -1:
                            dist[nr][nc][ntmod] = nt
                            q.append((nr, nc, nt))

    return -1
 
    pass


TC = int(input())
for test_case in range(1, TC+1):
    N = int(input())
    field = [list(map(int, input().split())) for _ in range(N)]
    sr, sc = map(int, input().split())
    er, ec = map(int, input().split())

    t = 0
    result = bfs(sr, sc, t)

    print(f'#{test_case} {result}')


    
