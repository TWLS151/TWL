# SWEA - 2105
# 디저트 카페

import sys
sys.setrecursionlimit(10**7)

directions = [
    (1, 1), (1, -1), (-1, -1), (-1, 1)
]

def route(r, c, d, cnt):
    global ans

    if d == 3 and r == row and c == col and cnt >= 4:
        ans = max(ans, cnt)
        return 
    
    for nd in (d, d+1):
        if nd >= 4:
            continue
        dr, dc = directions[nd]
        nr, nc = r + dr, c + dc

        if nr == row and nc == col and nd == 3 and cnt >= 3:
            route(nr, nc, nd, cnt + 1)
            continue

        if not (0 <= nr < N and 0 <= nc < N):
            continue

        idx = cafe[nr][nc]
        if visited[idx]:
            continue

        visited[idx] = True
        route(nr, nc, nd, cnt + 1)
        visited[idx] = False

    pass


TC = int(input())

for test_case in range(1, TC+1):
    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]

    ans = -1
    visited = [False] * 101

    for row in range(N):
        for col in range(N):
            visited[cafe[row][col]] = True
            route(row, col, 0, 0)
            visited[cafe[row][col]] = False

    print(f'#{test_case} {ans}')


'''

1. 방향 전환을 제한하는 방법
 # 구현하는데 방향을 먼저 정하고 들어가야하는데 그 방법을 생각해내지 못헀다.
 # 델타의 순서를 정하고 들어갈까 잠깐 생각했지만 실행하지는 않았고 결국 못했다.
 # 그냥 하자.

2. 기저 조건도 구현하지 못헀다.
 # 초기에 기저 조건을 시작점에 돌아오는 걸로 정해놓고 하긴 했지만
 # 구현하질 못했었다.

3. 방문처리의 방법
 # 처음에 집합을 이용해 중복 숫자를 피하려고 했었는데
 # 이렇게 카페 번호를 인덱스로 활용하는 방법도 있다는 걸 알았다.
 # 집합으로 처리하는 것도 틀린 방법은 아니다.
'''