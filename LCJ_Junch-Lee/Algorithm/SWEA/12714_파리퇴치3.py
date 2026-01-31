import sys
import os
sys.stdin = open("input.txt","r")

test_case = int(input())

for t in range(1, test_case + 1):
    
    N, M = map(int, input().split())
    
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    max_value = 0

    for i in range(N):
        for j in range(N):

            amount1, amount2 = (0,0)
            amount1 = arr[i][j]
            amount2 = arr[i][j]

            for d in range(1, M):

                for x, y in [(-1,0), (1,0), (0,-1), (0,1)]:
                    
                    ni = i + d * x
                    nj = j + d * y
                    
                    if 0 <= ni < N and 0 <= nj < N:
                        amount1 += arr[ni][nj]

                for x, y in [(-1, -1), (-1, 1), (1,-1), (1,1)]:

                    ni = i + d * x
                    nj = j + d * y

                    if 0 <= ni < N and 0 <= nj < N:
                        amount2 += arr[ni][nj]

                max_value = max(amount1, amount2, max_value)

    print(f'#{t} {max_value}')