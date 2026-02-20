# Baby-gin

from itertools import permutations, combinations
import sys
sys.stdin = open('input.txt')

# 순열
def isRun(arr):
    arr.sort()
    return arr[0] + 1 == arr[1] and arr[1] + 1 == arr[2]

def isTriple(arr):
    return len(set(arr)) == 1

TC = int(input())
for test_case in range(1, TC+1):
    nums = [int(i) for i in input()]

    result = 0

    for p in set(permutations(nums)):
        p1 = list(p[:3])
        p2 = list(p[3:])

        check1 = isRun(p1) or isTriple(p1)
        check2 = isRun(p2) or isTriple(p2)

        if check1 and check2:
            result = 1
            break

    print(f'#{test_case} {result}')

# --------------------- #

# 탐욕
TC = int(input())
for test_case in range(1, TC+1):
    nums = list(map(int, input()))

    counts = [0] * 10
    for i in nums:
        counts[i] += 1

    baby_gin_sets = 0

    for i in range(10):
        while counts[i] >= 3:
            counts[i] -= 3
            baby_gin_sets += 1

    for i in range(8):
        while counts[i] >= 1 and counts[i+1] >= 1 and counts[i+2] >= 1:
            counts[i] -= 1
            counts[i+1] -= 1
            counts[i+2] -= 1
            baby_gin_sets += 1

    result = 1 if baby_gin_sets >= 2 else 0

    print(f'#{test_case} {result}')

# -------------------------- #

# 탐욕 2
TC = int(input())
for test_case in range(1, TC+1):
    nums = list(map(int, input()))
    counts = [0] * 10
    for i in nums:
        counts[i] += 1

    baby_gin_sets = 0
    i = 0
    while i < 10:
        if counts[i] >= 3:
            counts[i] -= 3
            baby_gin_sets += 1
            continue

        if i <= 7 and counts[i] >= 1 and counts[i+1] >= 1 and counts[i+2] >= 1:
            counts[i] -= 1
            counts[i + 1] -= 1
            counts[i + 2] -= 1
            baby_gin_sets += 1
            continue

        i += 1

    result = 1 if baby_gin_sets == 2 else 0
    print(f'#{test_case} {result}')

# ----------------------- #

# 조합
def isRun(arr):
    arr.sort()
    return arr[0] + 1 == arr[1] and arr[1] + 1 == arr[2]

def isTriple(arr):
    return len(set(arr)) == 1

TC = int(input())
for test_case in range(1, TC+1):
    nums = list(map(int, input()))
    baby_gin = 0

    for group_lst in combinations(range(6), 3):

        group1 = []
        group2 = []
        for i in range(6):
            if i in group_lst:
                group1.append(nums[i])
            else:
                group2.append(nums[i])

        check1 = isRun(group1) or isTriple(group1)
        check2 = isRun(group2) or isTriple(group2)

        if check1 and check2:
            baby_gin =1
            break

    print(f'#{test_case} {baby_gin}')

# ----------------------- #

# 준혁님 코드

TC = int(input())
for test_case in range(1, TC+1):
    arr = list(map(int, list(input())))  ## ??
    baby_gin = 0

    arr.sort()

    idx = 0
    while idx < len(arr):
        if arr.count(arr[idx]) >= 3:
            for _ in range(3):
                arr.pop(idx)
            continue    
        idx += 1

    idx = 0
    arr = [nums - arr[0] for nums in arr]

    baby_gin = 1 if arr in [[], [0, 1, 2], \
                            [0, 0, 1, 1, 2, 2],\
                            [0, 1, 2, 3, 4, 5]] else 0
    
    print(f'#{test_case} {baby_gin}')