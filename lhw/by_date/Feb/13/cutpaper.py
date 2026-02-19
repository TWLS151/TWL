# BOJ 2628
# 종이자르기

import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())

t = int(input())

# 가로는 0
# 세로는 1

row = [0]
col = [0]
for _ in range(t):
    d, p = map(int, input().split())
    if d == 0:
        row.append(p)
    else:
        col.append(p)
row.sort()
col.sort()
row.append(M)
col.append(N)

# print(row, col)

best_row = 0
best_col = 0
if len(row) <= 1:
    best_row = row[0]
else:
    for i in range(len(row)-1):
        best_row = max(best_row, row[i+1] - row[i])
if len(col) <= 1:
    best_col = col[0]
else:
    for i in range(len(col)-1):
        best_col = max(best_col, col[i+1] - col[i])

print(best_row*best_col)