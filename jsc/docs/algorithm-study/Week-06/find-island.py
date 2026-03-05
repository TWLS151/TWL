import sys
from collections import deque

sys.stdin = open('find-island.txt')

N, M = map(int, input().split())

dr = [-1, 1, 0, 0, 1, 1, -1, -1]
dc = [0, 0, -1, 1, 1, -1, 1, -1 ]

# board = [list(map(int, input())) for _ in range(N)]
# visited = [[False] * M for _ in range(N)]
# q = deque([])
# cnt = 0

# for i in range(N):
#     for j in range(M):
#         if board[i][j] != 0 and visited[i][j] == False:
#             q.append((i, j))
#             visited[i][j] = True
#             cnt += 1

#             while q:
#                 cr, cc = q.popleft()
#                 for dir in range(8):
#                     nr, nc = cr + dr[dir], cc + dc[dir]

#                     if (0 <= nr < N and 0 <= nc < M) and board[nr][nc] != 0 and visited[nr][nc] == False:
#                         q.append((nr, nc))
#                         visited[nr][nc] = True

# print(cnt)

def dfs(r, c, N, board):

    visited[r][c] = True

    for dir in range(8):
        nr, nc = r + dr[dir], c + dc[dir]

        if 0 <= nr < N and 0 <= nc < N and board[nr][nc] == 1 and visited[nr][nc] == False:
            dfs(nr, nc, N, board)

    return True


    
    
    pass

board = [list(map(int, input())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

for i in range(N):
    for j in range(N):
        if board[i][j] == 1 and visited[i][j] == False:
            
            cnt = 0

            if dfs(i, j, N, board):
                print('1')