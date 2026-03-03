from collections import deque
import sys
sys.stdin = open('input.txt','r')

N, M = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(N)]

d = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

def in_range(x, y):
    return 0 <= x < y

path = []

def bfs_queue():

    visited = [[False]*M for _ in range(N)] # 방문 처리 행렬
    q = deque() # queue
    island = 0

    for i in range(N):
        for j in range(M):

            if arr[i][j] == 1 and not visited[i][j]: # 발견하지 않은 섬을 찾았다면

                path.append((i, j))
                q.append((i, j)) # queue에 push
                visited[i][j] = True # push와 함께 방문처리 (queue 중복 방지)
                island += 1

                while q: # queue가 빌 때 까지

                    r, c = q.popleft() # 저장된 위치의 행, 열값을 수신(언패킹)

                    for dr, dc in d: # 탐색할 5방향에 대해 좌표
                        nr = r + dr
                        nc = c + dc

                        if in_range(nr, N) and in_range(nc, M):
                            if not visited[nr][nc] and arr[nr][nc] == 1:
                                path.append((nr, nc))
                                q.append((nr, nc))
                                visited[nr][nc] = True

    return island

result = bfs_queue()

print(result)
print(path)





