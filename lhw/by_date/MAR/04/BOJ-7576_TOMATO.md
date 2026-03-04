# BOJ - 7576 _ 토마토

### [1] 정의
```
BFS

[1] STATE
토마토가 익었는지 안 익었는지

[2] CHOICE
익지 않았다면 익힌다.

[3] CONSTRAINT
가로, 세로 네 방향으로만 영향을 미친다.

[4] CHANGE, ROLLBACK
백트래킹 없음

[5] BASE LIST
BFS 종료
```

### [2] 코드
```python
import sys
from collections import deque

dirs = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]

def bfs(lst):
    global N, M, dist

    q = deque(lst)
    # dist[r][c] = 0  # 시작점 표시

    while q:
        r, c = q.popleft()

        for dr, dc in dirs:
            nr, nc = r+dr, c+dc

            if not (0 <= nr < N and 0 <= nc < M):
                continue

            if container[nr][nc] == -1:
                continue

            if dist[nr][nc] == None:
                dist[nr][nc] = dist[r][c] + 1

            # None 이면 간다.
            # 벽은 안간다.
            # 가려는 칸의 값이 내가 온 거리보다 크면 바꾸고
            # 더 작거나 같으면 그대로 둔다
            elif dist[nr][nc] > dist[r][c] + 1:
                dist[nr][nc] = dist[r][c] + 1

            else:
                continue
            q.append((nr, nc))


M, N = map(int, input().split())
already = True
container = []
for r in range(N):
    row = list(map(int, input().split()))
    if 0 in row:
        already = False
    container.append(row)

if already:
    print(0)
    sys.exit()

dist = [[None] * M for _ in range(N)]

done_lst = []

for r in range(N):
    for c in range(M):
        if container[r][c] == 1:  # 익은 토마토
            done_lst.append((r, c))
            dist[r][c] = 0
        if container[r][c] == -1:
            dist[r][c] = 0

bfs(done_lst)

worst = 0
for row in dist:
    if None in row:
        print(-1)
        sys.exit()

    worst = max(worst, max(row))

print(worst)
```