import sys
sys.stdin = open('swea_5105.txt')
from collections import deque


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def bfs(r, c, N, arr):
    distance = [[0] * N for _ in range(N)]
    q = deque([(r, c)])
    distance[r][c] = 1
    while q:
        r, c  = q.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0<= nr< N and 0<= nc< N and arr[nr][nc] != 1 and distance[nr][nc] == 0:
                if arr[nr][nc] == 3:
                    return distance[r][c] - 1
                distance[nr][nc] = distance[r][c] + 1
                q.append((nr, nc))
    return 0
    


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    start_r, start_c = -1, -1
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 2:
                start_r , start_c = r, c
                break
    result = bfs(start_r, start_c, N, arr)
    print(f'#{tc} {result}')


