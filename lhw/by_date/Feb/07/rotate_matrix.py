# SWEA - 1961
# 숫자 배열 회전

# 크기 N 의 행렬이 주어진다.
# 이 행렬을 시계 방향으로 90도 180도 270도 회전한 모양을 출력하라
# 3 <= N <= 7

import sys
sys.stdin = open('rotate_matrix.txt')

TC = int(input())

def rotation(matrix):
    pass

    rotated_matrix = [[0] * N for _ in range(N)]

    for j in range(N):
        for i in range(N):
            rotated_matrix[i][j] = matrix[j][N-1-i]

    return rotated_matrix


for test_case in range(1, TC+1):
    N = int(input())
    matrix = [list((map(int, input().split()))) for _ in range(N)]

    matrix90 = rotation(matrix)
    matrix180 = rotation(matrix90)
    matrix270 = rotation(matrix180)

    print(f'#{test_case}')
    for x, y, z in zip(matrix90, matrix180, matrix270):
        print(f"{''.join(map(str, x))} {''.join(map(str, y))} {''.join(map(str, z))}")