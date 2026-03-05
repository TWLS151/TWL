# ===
# 최소칸의 숫자 => BFS로 풀면된다.
# 그런데 DFS로 풀자
# DFS에 대해서 많은 인사이트를 얻은 문제 나중에 다시 풀자.
# 리턴 값이 불리언이 아나라 다른 값을 가져올 때 어떻게 코드를 구성을 할지
# 생각을 할 필요성이 있다.
# ===

import sys

sys.stdin = open('swea-5105.txt')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c, N, visited, cnt):
    if board[r][c] == 3:
        return cnt - 1
    
    visited[r][c] = True

    for dir in range(4):
        nr, nc = r + dr[dir], c + dc[dir]

        if 0 <= nr < N and 0 <= nc < N:
            if visited[nr][nc] == False and board[nr][nc] !=1:
                result =  dfs(nr, nc, N, visited, cnt + 1)
                if result > 0:
                    return result
    return 0
        

    pass


T = int(input())

for tc in range(1, T+1):
    N = int(input())

    board = [list(map(int, input())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                start_r, start_c = i, j
                break

    cnt = 0

    # 여기서 많이 배웠다.
    # 나는 DFS를 쓴다면 if dfs호출 함수 이런식으로 많이 썼다.
    # 그런데 지금 상황에서는 쓸 수가 없다.
    # 왜냐하면 도착했냐 안했냐가 아니라 얼마나 걸렸는지 즉 불리언이 아닌 다른 정보를
    # 받아야했기 때문이다.
    ans = dfs(start_r, start_c, N, visited, cnt)
    print(ans)