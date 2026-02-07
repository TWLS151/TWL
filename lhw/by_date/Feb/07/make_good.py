# SWEA - 4466
# 최대 성적표 만들기

import sys
sys.stdin = open('make_good.txt')


TC = int(input())

for test_case in range(1, TC+1):
    N, K = map(int, input().split())
    score_lst = list(map(int, input().split()))
    pass

    score_lst.sort(reverse= True)

    print(f'#{test_case} {sum(score_lst[:K])}')
    