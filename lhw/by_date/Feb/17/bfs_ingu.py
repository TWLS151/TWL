# BOJ - 16234
# 인구 이동

import sys
sys.stdin = open('input.txt')

from collections import deque

dirs =[
    (-1, 0), (1, 0), (0, -1), (0, 1)
]

def bfs():

    count = 0
    visited = [[-1] * N for _ in range(N)]
    visited[0][0] = -1
    next = deque([(0, 0)])
    while True:
        for sr, sc in next:
            if visited[sr][sc] == -1:
                q = deque([(sr, sc)])

        while q:
            r, c = q.popleft()
            total = kunis[r][c]
            aver = [(r, c)]
            
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc

                if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == -1:
                    if L <= abs(kunis[nr][nc] - kunis[r][c]) <= R:
                        visited[nr][nc] = count
                        q.append((nr, nc))
                        aver.append((nr, nc))
                        total += kunis[nr][nc]
                    else:
                        next.appendleft((nr, nc))
        
        average = total // len(aver)
        for i, j in aver:
            kunis[i][j] = average
        
        count += 1

        if not next:
            return count




N, L, R = map(int, input().split())
kunis = [list(map(int, input().split())) for _ in range(N)]

print(bfs())