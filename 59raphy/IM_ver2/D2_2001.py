import sys

sys.stdin = open('input_2001.txt')

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    max_fly = 0

    for r in range(N):
        for c in range(N):
            fly_cnt = 0
            for i in range(M):
                for j in range(M):
                    if 0 <= r + i < N and 0 <= c + j < N:
                        fly_cnt += matrix[r + i][c + j]
            if max_fly < fly_cnt:
                max_fly = fly_cnt

    print(f'#{test_case} {max_fly}')
