# SWEA - 4008
# 숫자 만들기

import sys
import itertools
from copy import deepcopy

sys.stdin = open('input.txt')

def cal(val1, val2, oper):
    if oper == '+':
        return val1 + val2
    elif oper == '-':
        return val1 - val2
    elif oper == '*':
        return val1 * val2
    else:
        return int(val1 / val2)
    pass

def dfs(l, val):
    global max_val, min_val
    if l == n-1:
        max_val = max(max_val, val)
        min_val = min(min_val, val)

    else:
        for i in range(4):
            if op[i] > 0:
                op[i] -= 1
                res_val = cal(val, nums[l+1], operators[i])
                dfs(l+1, res_val)
                op[i] += 1

operators = ['+', '-', '*', '/']
T = int(input())
for t in range(1, T+1):
    n = int(input())
    op = list(map(int, input().split()))
    nums = list(map(int, input().split()))

    max_val = -10**8
    min_val = 10**8
    dfs(0, nums[0])

    print(f'#{t} {max_val - min_val}')



# ---------------------------------------- #

# def cal(lst, ops):

#     for i in ops:
#         b = lst.pop()
#         a = lst.pop()
#         try:
#             if i == '+':
#                 lst.append(a + b)
#             elif i == '-':
#                 lst.append(a - b)
#             elif i == '*':
#                 lst.append(a * b)
#             else:
#                 lst.append(int(a/b))
#         except ZeroDivisionError:
#             continue

#     return lst.pop()

#     pass

# TC = int(input())
# for test_case in range(1, TC+1):
#     N = int(input())
#     op = list(map(int, input().split()))
#     nums = list(map(int, input().split()))

#     ops = ''
#     ops += '+' * op[0]
#     ops += '-' * op[1]
#     ops += '*' * op[2]
#     ops += '/' * op[3]

#     order = set(itertools.permutations(ops, len(ops)))
#     # 중복 없이 순열 생성
    
#     nums.reverse()

#     backup = nums
#     min_val = 10**8
#     max_val = -10**8
#     for i in order:
#         backup = deepcopy(nums)
#         result = cal(backup, i)
#         if min_val > result:
#             min_val = result
#         if max_val < result:
#             max_val = result

#     print(f'#{test_case} {max_val - min_val}')