import sys

sys.stdin = open('swea_2001_파리 퇴치.txt')
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_val = 0
    for r in range(N):
        for c in range(N):
            sum_val = 0
            for dr in range(M):
                for dc in range(M):
                    if 0<= r + dr < N and 0<= c+dc < N:
                        sum_val += arr[r+dr][c+dc]
            if max_val < sum_val:
                max_val = sum_val
    print(f'#{tc} {max_val}')