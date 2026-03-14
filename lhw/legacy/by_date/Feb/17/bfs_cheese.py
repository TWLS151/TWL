# BOJ - 2636
# 치즈

# (0, 0) 에서 bfs 방문처리로 외부 공간 다 찾고
# 한 칸 붙어있는 부분만 치즈 없애고
# 다시 찾고 없애고 반복

import sys
sys.stdin = open('input.txt')

from collections import deque

dirs = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]

def bfs():
    global N, M, cheese, cheese_count


    
    time = 0

    while True:

        q = deque([(0, 0)])
        visited = [[False] * M for _ in range(N)]
        visited[0][0] = True
        visited_cheese = 0
        
        while q:
            
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc

                if 0 <= nr < N and 0 <= nc < M:
                    if cheese[nr][nc] == 0 and not visited[nr][nc]:
                        q.append((nr, nc))
                        visited[nr][nc] = True
                    if cheese[nr][nc] == 1:
                        visited[nr][nc] = True
                      
        for i in range(N):
            for j in range(M):
                if visited[i][j] and cheese[i][j] == 1:
                    cheese[i][j] = 0
                    visited_cheese += 1

        if cheese_count - visited_cheese != 0:
            cheese_count -= visited_cheese
        else:
             return time+1, cheese_count               
        time += 1

    pass

N, M = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(N)]

cheese_count = 0
for r in range(N):
    for c in range(M):
        if cheese[r][c] == 1:
            cheese_count += 1

time, num = bfs()
print(time)
print(num)