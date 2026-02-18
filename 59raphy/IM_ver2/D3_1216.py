import sys

sys.stdin = open('input_1216.txt')

T = 10

def find_palindrom(matrix, t_matrix):
    for i in range(100, 1, -1):
        for r in range(100):
            for c in range(101-i):
                row_word = matrix[r][c:c+i]
                if row_word == row_word[::-1]:
                    return i
                col_word = t_matrix[r][c:c+i]
                if col_word ==col_word[::-1]:
                    return i
    return 1

for test_case in range(1, T + 1):
    N = int(input())
    matrix = [input() for _ in range(100)]
    t_matrix = list(zip(*matrix))

    print(f'#{test_case} {find_palindrom(matrix, t_matrix)}')
