# BOJ - 2175
# 미로 탐색

# 최단거리 찾기

import sys
sys.stdin = open('input.txt')

from collections import deque

N, M = map(int, input().split())
maze = [input() for _ in range(N)]

# (0, 0) 에서 (N, M) 으로
# 1은 길, 0은 벽

dirs = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]

def bfs():

    q = deque()
    q.append((0, 0))
    dist = [[0]*M for _ in range(N)]
    dist[0][0] = 1

    while q:
        pr, pc = q.popleft()
        for idx in range(4):
            dr, dc = dirs[idx]
            r, c = pr+dr, pc+dc

            if 0<=r<N and 0<=c<M and maze[r][c] == '1' and dist[r][c] == 0:
                q.append((r, c))
                dist[r][c] = dist[pr][pc] + 1
    
    return dist[N-1][M-1]

print(bfs())