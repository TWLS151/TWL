import sys

sys.stdin = open('swea_1209_Sum.txt')

for tc in range(1, 11):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    max_val = 0 # 출력값 미리 지정
    # 가로, 세로, 대각선 합을 구하고 더 큰값이 나오면 대체하는 방식
    for r in range(100):
        row_sum = 0
        column_sum = 0
        for c in range(100):
            row_sum += arr[r][c]
            column_sum += arr[c][r]
        if max_val < row_sum:
            max_val = row_sum
        if max_val < column_sum:
            max_val = column_sum
    diagonal_sum1, diagonal_sum2 = 0, 0
    for i in range(100):
        diagonal_sum1 += arr[i][i]
        diagonal_sum2 += arr[i][99-i]
        if max_val < diagonal_sum1:
            max_val = diagonal_sum1
        if max_val < diagonal_sum2:
            max_val = diagonal_sum2
    print(f'#{tc} {max_val}')