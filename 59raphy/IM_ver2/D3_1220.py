import sys

sys.stdin = open('input_1220.txt')

T = 10

for test_case in range(1, T + 1):
    N = int(input())
    table = [input().split() for _ in range(N)]

    deadlock_cnt = 0

    for c in range(N):
        last_magnet = 0
        for r in range(N):
            if table[r][c] == '1':
                last_magnet = 1
            elif table[r][c] == '2':
                if last_magnet == 1:
                    deadlock_cnt += 1
                last_magnet = 2

    print(f'#{test_case} {deadlock_cnt}')
