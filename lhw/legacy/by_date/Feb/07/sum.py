# SWEA - 1209
# SUM

# TTP: 19' 14"

import sys
sys.stdin = open('sum.txt')

TC = 10

for test_case in range(1, TC+1):
    test_num = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]

    # 행과 열
    row_total = max_row = 0
    col_total = max_col = 0
    for row in range(100):
        for col in range(100):
            row_total += matrix[row][col]
            col_total += matrix[col][row]
        if max_row < row_total:
            max_row = row_total
        if max_col < col_total:
            max_col = col_total
        row_total = col_total = 0

    # 대각선
    rdaegak_total = 0
    ldaegak_total = 0
    for i in range(100):
        # for j in range(100-1, -1, -1):
            rdaegak_total += matrix[i][i]
            ldaegak_total += matrix[i][99 - i]

    print(f'#{test_num} {max(max_col, max_row, rdaegak_total, ldaegak_total)}')