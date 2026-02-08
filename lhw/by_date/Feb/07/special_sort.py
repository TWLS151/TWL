# SWEA - 4843
# 특별한 정렬

import sys
sys.stdin = open('special_sort.txt')

TC = int(input())

for test_case in range(1, TC+1):
    N = int(input())
    num_lst = list(map(int, input().split()))
    pass

    # just_sort
    # for i in range(N-1):
    #     for j in range(i+1, N):
    #         if num_lst[i] > num_lst[j]:
    #             num_lst[i], num_lst[j] = num_lst[j], num_lst[i]
    
    # bubble
    # for i in range(N-1, -1, -1):
    #     for j in range(i):
    #         if num_lst[j] > num_lst[j+1]:
    #             num_lst[j], num_lst[j+1] = num_lst[j+1], num_lst[j]
    
    # select
    for i in range(N-1):
        min_idx = i
        for j in range(i+1, N):
            if num_lst[j] < num_lst[min_idx]:
                min_idx = j
        num_lst[i], num_lst[min_idx] = num_lst[min_idx], num_lst[i]
    
    result = []
    for i in range(5):
        result.append(num_lst[-i-1])
        result.append(num_lst[i])
    
    print(f'#{test_case}', *result)