# BOJ - 1388
# 바닥 장식
# 구현, 그래프

from collections import deque

dirs = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]


N, M = map(int, input().split())
field = [list(input()) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
count = 0

def cango(r, c, nr, nc):

    if not (0 <= nr < N and 0 <= nc < M):
        return False
    
    if visited[nr][nc]:
        return False
    
    if field[nr][nc] != field[r][c]:
        return False
    
    return True

    pass

def bfs(r, c):
    global count

    q = deque([(r, c)])
    visited[r][c] = True
    
    while q:
        r, c = q.popleft()

        if field[r][c] == '|':
            dir_lst = [0, 1]
        else:
            dir_lst = [2, 3]
        
        for idx in dir_lst:
            dr, dc = dirs[idx]
            nr, nc = r+dr, c+dc

            if cango(r, c, nr, nc):
                q.append((nr, nc))
                visited[nr][nc] = True

    pass


for r in range(N):
    for c in range(M):
        if not visited[r][c]:
            bfs(r, c)
            count += 1

print(count)

