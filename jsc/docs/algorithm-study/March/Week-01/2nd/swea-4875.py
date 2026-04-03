import sys
from collections import deque
sys.stdin = open('swea-4875.txt')


T = int(input())

# 1. 기본값 세팅: 보드, 인풋 받기
for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    q = deque()
    result = 0

    # 2. 시작 위치 찾기
    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                curr_r= i
                curr_c = j
                q.append((i, j))

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 3. BFS 탐색 시작
    while q:
        curr_r, curr_c = q.popleft()

        # 정지조건
        if board[curr_r][curr_c] ==3:
            result = 1
            break
        
        for dir in range(4):                        
            now_r = curr_r + dr[dir]
            now_c = curr_c + dc[dir]

            if (0 <= now_r < N and 0 <= now_c < N) and board[now_r][now_c] != 1 and visited[now_r][now_c] == False:
                # 방문처리
                visited[now_r][now_c] = True
                q.append((now_r, now_c))
                
    
    print(result)



    