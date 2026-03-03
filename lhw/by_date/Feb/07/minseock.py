# SWEA - 5431
# 민석이의 과제 체크하기

import sys
sys.stdin = open('minseock.txt')

TC = int(input())

for test_case in range(1, TC+1):
    whole, part = map(int, input().split())
    part_num = list(map(int, input().split()))
    pass

    whole_lst = [num for num in range(1, whole+1)]

    for num in part_num:
        whole_lst.remove(num)

    print(f'#{test_case}', *whole_lst)