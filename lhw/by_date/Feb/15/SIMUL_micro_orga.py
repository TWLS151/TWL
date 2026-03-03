# SWEA - 2382
# 미생물 격리

# 한시간마다 이동
# 가장자리에 닿으면 절반 죽고 방향 반대
# 두개 이상의 군집이 모이면 합쳐지고
# 수는 그대로 합하고 방향은 가장 큰 군집의 방향

import sys
sys.stdin = open('input.txt')

dirs = [
    (0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)
]

rev = {1: 2, 2: 1, 3: 4, 4: 3}

TC = int(input())
for test_case in range(1, TC+1):
    N, M, K = map(int, input().split())
    field = [[0]*N for _ in range(N)]
    ameba = [list(map(int, input().split())) for _ in range(K)]

    info = {}
    for r, c, num, d in ameba:
        info[(r, c)] = [num, d]

    for t in range(1, M+1):
        for r, c, num, d in ameba:
            dr, dc = dirs[d]
            nr, nc = r + dr, c + dc
            # 다음 포지션 nr, nc
            if nr == 0 or nr == N-1 or nc == 0 or nc == N-1:
                num //= 2
                d = rev[d]
            if (nr, nc) in info.keys():
                info[(nr, nc)] += [num, d]
                info[(r, c)] = 0
            else:
                info[(nr, nc)] = [num, d]
                info[(r, c)] = 0
        
        for (r, c) in info:
            total = 0
            if len(info[(r, c)]) >= 2:
                for num, d in info[(r, c)]:
                    total += num
                info[(r, c)] = [total, d]