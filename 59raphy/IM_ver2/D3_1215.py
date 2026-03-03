import sys

sys.stdin = open('input_1215.txt')

T = 10

for test_case in range(1, T + 1):
    N = int(input())
    # 문자열은 그 자체로 인덱싱, 슬라이싱 가능하므로 리스트로 변환할 필요 없음
    matrix = [input() for _ in range(8)]
    # 수정이 불필요한 작업에서는 zip이 반환한 튜플을 다시 리스트로 변환할 필요 없음
    t_matrix = list(zip(*matrix))

    palindrome_cnt = 0
    M = N // 2

    for r in range(8):
        for c in range(9-N):
            if matrix[r][c:c+M] == matrix[r][c+N-1:c+N-1-M:-1]:
                palindrome_cnt += 1
            if t_matrix[r][c:c+M] == t_matrix[r][c+N-1:c+N-1-M:-1]:
                palindrome_cnt += 1

    print(f'#{test_case} {palindrome_cnt}')
