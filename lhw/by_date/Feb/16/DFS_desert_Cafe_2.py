# SWEA - 2105
# 디저트 카페
# 2회차

import sys
sys.stdin = open('input.txt')

# 대각선 방향으로 움직인다
directions = [
    (1, 1), (1, -1), (-1, -1), (-1, 1)
]

# 출발지점으로 돌아와야한다  ==  기저조건
# 같은 숫자의 디저트는 안된다  ==  중복x
# 가장 많이 먹을 수 있는 경로, 그 때 디저트의 수  ==  DFS 힌트
# 못먹으면 -1 출력

def dfs(row, col , route, d, sr, sc):


    # 기저조건 = 출발지점으로 돌아온다. // 같은자리를 돌면 안된다.
    if row == sr and col == sc and len(route) >= 4 and d == 3:
        return len(route)

    # 할 일
    # 한 바퀴 도는거
    # 방향을 제한해야함 ( 마름모를 그려야하니까 )
    count = -1
    for idx in (d, d+1):
        if idx > 3:
            continue

        dr, dc = directions[idx]
        nr, nc = row + dr, col + dc
        # 진입 조건
        # 1. 지도 안이어야함
        # 2. 중복 x
        # 3. 시작점으로 돌아가는건 예외 허용해야함

        if 0<= nr < N and 0<= nc < N:
            if nr == sr and nc == sc:
                count = max(count, dfs(nr, nc, route, idx, sr, sc))
            else:
                if cafes[nr][nc] not in route:
                    route.add(cafes[nr][nc])
                    count = max(count, dfs(nr, nc, route, idx, sr, sc))
                    route.remove(cafes[nr][nc])
    return count


TC = int(input())
for test_case in range(1, TC+1):
    N = int(input())
    cafes = [list(map(int, input().split())) for _ in range(N)]

    
    max_result = -1

    for sr in range(N):
        for sc in range(N):
            route = set()
            route. add(cafes[sr][sc])
            result = dfs(sr,sc,route,0,sr,sc)
            if max_result < result:
                max_result = result
    
    print(max_result)