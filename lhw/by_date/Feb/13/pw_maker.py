# SWEA - 1225
# 암호생성기

import sys
from collections import deque

sys.stdin = open('input.txt')

for tc in range(1, 11):
    tcnum = int(input())
    nums = deque(map(int, input().split()))
    
    # print(nums[-1])
    # end = nums[-1]

    idx = 0
    plus = list(range(1, 6))
    while nums[-1] > 0:
        
        i = plus[idx % 5]

        nums.append(nums.popleft() - i)

        idx += 1

    nums[-1] = 0

    print(f'#{tc}', *nums)