# SWEA - 4013
# 특이한 자석

import sys
sys.stdin = open('input.txt')

from collections import deque

TC = int(input())
for test_case in range(1, TC+1):
    K = int(input())
    topnis = [0] + [deque(map(int, input().split())) for _ in range(4)]

    for _ in range(K):
        n, d = map(int, input().split())

        rot = [0] * 5
        rot[n] = d

        for i in range(n, 1, -1):
            if topnis[i][6] != topnis[i-1][2]:
                rot[i-1] = -rot[i]
            else:
                break

        for i in range(n, 4):
            if topnis[i][2] != topnis[i+1][6]:
                rot[i+1] = -rot[i]
            else:
                break

        for i in range(1, 5):
            topnis[i].rotate(rot[i])

    score = 0
    for i in range(1, 5):
        if topnis[i][0] == 1:
            score += 2 ** (i-1)

    print(f"#{test_case} {score}")