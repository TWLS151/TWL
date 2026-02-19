# 출출
# 0212 // 1315 - 1438 // 1차 실패 : 풀 수 있을 것 같아서 나중에 다시 풀 예정

import sys
sys.stdin = open('a.txt')

TC = int(input())
for test_case in range(1, TC+1):
    N, M, K = map(int, input().split())

    X = N - M

    lst = list(range(0, N+1, K))[1:]

    if N - M >= len(lst):
        score = M
        
    else:
        for _ in range(X):
            lst.pop()

        count = 0
        score = 0
        for i in range(1, M+1):
            count += 1
            score += 1
            if count in lst:
                score *= 2

    
    print(f'#{test_case} {score}')