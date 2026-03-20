#===
# swea-1486
# 장훈이의 높은 선반
# ===

import sys
from itertools import combinations

sys.stdin = open('swea-1486.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    array = list(map(int, input().split()))

    # 높이가 특정 높이 이상 중에서 가장 낮은것을 골라야한다.
    # combination을 사용을 해서 최저값을 구해도 된다
    # dfs를 사용을 해도 된다. 다만 책높이와 같을 때 break를 걸자.

    # solve 1. combination 풀이
    # 생각을 해보니 몇개를 뽑아야하는지 안정해져 있어서 인원이 많아지면
    # 런타임이 좀 걸릴 것 같다. 반복문으로 하면 될듯.
    # 해볼까? 아니면 dfs로 갈까?
    all_list = []
    # 
    for attend_num in range(1, N+1):
        combin = list(combinations(array, attend_num))
        all_list.extend([list(c) for c in combinations(array, attend_num)])
        
    print(all_list)
        # print(combin)
    total = 0
    for i in range(len(all_list)):
        combin[0][i]
        if combin >= M:
            # 새 리스트에 추가
            # # 새 값 갱신


        total += combin[0][i]
    print(total)

        # for person_num in range(N):
        #     for person_height in list_0:
                # print(combin[person_num])
                # list_0.append(combin[person_num])
                # print(list_0)
