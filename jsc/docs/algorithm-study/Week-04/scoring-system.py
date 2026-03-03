"""
슈도 코드
max_total = float('-inf')
min_total = float('inf')
def
for man in matrix:
    for j man in matrix[i]:
        if j == 1:
            cnt += 1
            total += cnt
        else:
            cnt = 0
    if total >= max_cnt:
        max_cnt = total
    if total <= min_cnt:
        min_cnt = total

print(max_cnt)
print(min_cnt)

"""

import sys

sys.stdin = open('scoring-system.txt')

T = int(input())

N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]

max_total = float('-inf')
min_total = float('inf')


for man in matrix:
    cnt = 0
    total = 0
    for score in man:
        if score == 1:
            cnt += 1
            total += cnt
        else:
            cnt = 0
    if total >= max_total:
        max_total = total
    if total <= min_total:
        min_total = total

print(max_total)
print(min_total)