# SWEA - 26045
# 부분 수열 판별

import sys
sys.stdin = open('part_array.txt')

TC = int(input())

for test_case in range(1, TC+1):
    N, M = map(int, input().split())
    a_arr = list(map(int, input().split()))
    b_arr = list(map(int, input().split()))

    a_pointer, b_pointer = 0, 0
    while a_pointer < N and b_pointer < M:
        if a_arr[a_pointer] == b_arr[b_pointer]:
            b_pointer += 1
        a_pointer += 1
    
    print(f'#{test_case}', 'YES' if b_pointer == M else 'NO')











    # limit = 0
    # fail = 0
    # for i in range(M):
    #     found = 0
    #     for j in range(limit, N):
    #         if a_arr[j] == b_arr[i]:
    #             limit = j + 1
    #             found += 1
    #             break
    #     if found == 0:
    #         print(f'#{test_case} NO')
    #         fail += 1
    #         break
    # if fail == 0:
    #     print(f'#{test_case} YES')