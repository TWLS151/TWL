# BOJ - 14500
# 테트로미노
import time

start = time.perf_counter()

# import sys
# input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 보드에서 4 칸의 합이 가장 큰 구역을 찾고 그 합을 출력해라.

dirs = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]

def dfs(r, c, l, val):
    global max_val

    if l == 4:
        max_val = max(max_val, val)
        return

    for dr, dc in dirs:
        nr, nc = r+dr, c+dc

        if 0 <= nr < N and 0 <= nc < M:
            if not visited[nr][nc]:
                visited[nr][nc] = True
                dfs(nr, nc, l+1, val+board[nr][nc])
                visited[nr][nc] = False

def iron(r, c, val):
    global max_val

    for idx in range(4):
        nval = val
        for i in range(3):
            dr, dc = dirs[(idx+i) % 4]
            nr, nc = r+dr, c+dc
    
            if 0 <= nr < N and 0 <= nc < M:
                nval += board[nr][nc]
    
        max_val = max(max_val, nval)

    pass


visited = [[False]*M for _ in range(N)]

max_val = 0

for r in range(N):
    for c in range(M):
        visited[r][c] = True
        dfs(r, c, 1, board[r][c])
        visited[r][c] = False
        iron(r, c, board[r][c])

print(max_val)

end = time.perf_counter()
print(end-start)