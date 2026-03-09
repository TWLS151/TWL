import sys

sys.stdin = open('input_4613.txt')

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    flag = [input() for _ in range(N)]

    min_paint = N * M

    for i in range(1, N-1):
        for j in range(i+1, N):
            paint_cnt = 0
            for c in range(M):
                for r in range(i):
                    if flag[r][c] != 'W':
                        paint_cnt += 1
                for r in range(i, j):
                    if flag[r][c] != 'B':
                        paint_cnt += 1
                for r in range(j, N):
                    if flag[r][c] != 'R':
                        paint_cnt += 1
            if min_paint > paint_cnt:
                min_paint = paint_cnt

    print(f'#{test_case} {min_paint}')
