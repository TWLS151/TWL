import sys
sys.stdin = open('swea_4836_색칠하기.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * 10 for _ in range(10)]
    count = 0
    for i in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                arr[r][c] += color
    for r in range(10):
        for c in range(10):
            if arr[r][c] == 3:
                count += 1
    print(f'#{tc} {count}')
   