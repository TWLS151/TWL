# BOJ - 2669
# 직사각형 네개의 합집합의 면적 구하기

import sys
sys.stdin = open('input.txt')

gragh = [[0 for _ in range(100)] for _ in range(100)]

for _ in range(4):
    a, b, c, d = map(int, input().split())

    for row in range(100):
        for col in range(100):
            if a <= row < c and b <= col < d:
                gragh[row][col] += 1

count = 0
for row in range(100):
    count += gragh[row].count(0)

print(100*100 - count)