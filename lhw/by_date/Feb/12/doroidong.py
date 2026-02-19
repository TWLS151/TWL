from collections import deque

directions = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]

def bfs(grid, N, M):

    distance = [[-1] * M for _ in range(N)]

    q = deque([(0, 0)])
    distance[0][0] = 0

    while q:
        r, c = q.popleft()

        if r == N -1 and c == M-1:
            return distance[r][c]
        
        for i in range(4):
            dr, dc = directions[i]
            nr, nc = r + dr, c +dc

            if (
                0<= nr <N and
                0<= nc <M and
                grid[nr][nc] == 1 and
                distance[nr][nc] == -1
            ):
                
                distance[nr][nc] = distance[r][c] + 1
                q.append((nr, nc))



N, M = map(int, input().split())
grid = [list(map(int, input())) for _ in range(N)]

result = bfs(grid, N, M)
print(result)