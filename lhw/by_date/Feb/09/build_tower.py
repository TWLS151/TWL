# IM
# 탑 쌓기

import sys
sys.stdin = open('build_tower.txt')

import itertools

TC = int(input())

for test_case in range(1, TC+1):
    baggage_num, height1, height2 = map(int, input().split())
    weight = list(map(int, input().split()))

    weight.sort()
    # 높이1, 높이2 의 크기만큼 나눠 담아야하는데
    # 무작위로 골라 담아낸다.
    lst = list(itertools.combinations(weight, height1))

    mul_lst = []

    
    for i in lst:
        add_lst = []
        height11 = height1
        height22 = height2
        for w in weight:
            if w in i:
                add_lst.append(w*height11)
                height11 -= 1
            else:
                add_lst.append(w*height22)
                height22 -= 1

        mul_lst.append(sum(add_lst))


    print(min(mul_lst))    

