# SWEA - 4012
# 요리사

import sys
sys.stdin = open('input.txt')

from itertools import combinations

# N 개의 식재를 반반 나누어 두개의 요리를 만든다.
# combinations(ingredient, N//2)


TC = int(input())
for test_case in range(1, TC+1):
    N = int(input())
    chart = [list(map(int, input().split())) for _ in range(N)]
    ingredient = list(range(N))
    min_diff = float('inf')

    for a in combinations(ingredient, N//2):
        b = list(set(ingredient) - set(a))
        # print(a, b)

        score_a = 0
        score_b = 0

        for i, j in combinations(a, 2):
            score_a += chart[i][j] + chart[j][i]
        
        for i, j in combinations(b, 2):
            score_b += chart[i][j] + chart[j][i]

        min_diff = min(min_diff, abs(score_a - score_b))
    
    print(f'#{test_case} {min_diff}')



# recur

def find_min_diff(k, a_count, start_idx):
    global min_diff
    
    if k == a_count:

        score_a, score_b = 0, 0
        group_a, group_b = [], []

        for i in range(N):
            if selected[i]:
                group_a.append(i)
            else:
                group_b.append(i)
            
        for i in range(a_count):
            for j in range(i+1, a_count):
                score_a += (
                    chart[group_a[i]][group_a[j]]
                    + chart[group_a[j]][group_a[i]]
                )
                score_b += (
                    chart[group_b[i]][group_b[j]]
                    + chart[group_b[j]][group_b[i]]
                )

        min_diff = min(min_diff, abs(score_a - score_b))
        return

    for i in range(start_idx, N):
        selected[i] = True
        find_min_diff(k+1, a_count, i+1)
        selected[i] = False
    
    pass

TC = int(input())
for test_case in range(1, TC+1):
    N = int(input())
    chart = [list(map(int, input().split())) for _ in range(N)]

    selected = [False] * N
    min_diff = float('inf')

    find_min_diff(0, N//2, 0)

    print(f'#{test_case} {min_diff}')