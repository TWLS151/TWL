# SWEA - 1216
# 가장 긴 회문 찾기

# IDEA
# 1. 역순탐색
# 2. 전치로 행만 두 번 탐색
# 3. 완전탐색

# 행을 돌며 길이를 배열의 길이부터 하나씩 줄여가며 슬라이딩 윈도우

def LongestPalindrome(matrix):
    pass
    
    max_len = 0
    for row in matrix:

        for lenghth in range(100, -1, -1):

            # length가 M일 때 0부터 M-1까지는 탐색해야함
            for start in range(100 - lenghth + 1):

                end = start + lenghth

                if row[start : end + 1][::-1] == row[start : end + 1]:
                    palin_len = len(row[start : end + 1])
                    if max_len < palin_len:
                        max_len = palin_len
                    continue
    return max_len


for test_case in range(1, 11):
    tc = input().strip()
    matrix = [[i for i in input()] for _ in range(100)]

    max_len = 0
    # 첫 매트릭스
    row_max = LongestPalindrome(matrix)
    if max_len < row_max:
        max_len = row_max

    # 전치
    new_matrix = list(map(list, zip(*matrix)))

    # 둘 매트릭스
    col_max = LongestPalindrome(new_matrix)
    if max_len < col_max:
        max_len = col_max

    print(f'#{tc} {max_len}')
