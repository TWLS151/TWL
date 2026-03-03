# SWEA - 1209
# Sum

# 1. base case
# 언제 끝나긴 계산 다 하면 멈춰야지
# 행 열 대각선으로 나누자
# if i == height:
#   return [i][j]
# if j == width:
#   return [i][j]


# 2. recurse
# [i][j] + [i][j+1]
# [i][j] + [i+1][j]

import sys
sys.stdin = open('cur5.txt')
sys.setrecursionlimit(10**7)

def rowSum(row, col):
    if col == 99:
        return matrix[row][col]
    
    return matrix[row][col] + rowSum(row, col+1)
    
def colSum(row, col):
    if row == 99:
        return matrix[row][col]
    
    return matrix[row][col] + colSum(row+1, col)

def kSum(row, col):
    if row == 99:
        return matrix[row][col]
    
    return matrix[row][col] + kSum(row + 1, col + 1)

def sumK(row, col):
    if row == 99:
        return matrix[row][col]
    
    return matrix[row][col] + sumK(row + 1, col - 1)
        

TC = 10

for test_Case in range(1, 11):
    test_num = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]

    max_row = 0
    max_col = 0
    max_k = 0
    for i in range(100):
        max_row = max(max_row, rowSum(i,0))
        max_col = max(max_col, colSum(0,i))
    max_k = max(max_k, kSum(0, 0), sumK(0, 99))

    print(f'#{test_num} {max(max_row, max_col, max_k)}')
