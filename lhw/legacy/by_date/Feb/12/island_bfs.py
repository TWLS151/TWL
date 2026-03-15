from collections import deque

directions = [
    (-1, 0), (1, 0), (0, -1), (0, 1),
    (-1, -1), (-1, 1), (1, -1), (1, 1)
]

def bfs(row, col):

    visited[row][col] = True
    q = deque()

    q.append((row, col))

    while q:

        r, c = q.popleft()
        for dr, dc in directions:
            nr, nc = r+dr, c+dc

            if (
                0 <= nr < N and
                0 <= nc < M and
                not visited[nr][nc] and
                tizu[nr][nc] == 1
                ):
                visited[nr][nc] = True
                q.append((nr, nc))

    pass


N, M = map(int, input().split())
tizu = [list(map(int, input())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

count = 0
for row in range(N):
    for col in range(M):
        if not visited[row][col] and tizu[row][col] == 1:
            count += 1
            bfs(row, col)

print(count)