# SWEA - 5356
# 의석이의 세로로 말해요

# 매트릭스 다 만들고 그냥 순회하면 되겠네

# 인풋부터 받고

tc = int(input())

for test_case in range(1, tc+1):
    word_num = 5
    word_lst = [input() for _ in range(5)]
    # print( word_lst)

    # 단어 글자수는 15까지 있다는데 전부 다 만들기는 좀 낭비같네
    # 최대 길이 먼저 찾고 그 길이로 만들자
    max_len = 0
    for word in word_lst:
        if max_len < len(word):
            max_len = len(word)

		# --------- 폐기 --------- #

    # # 이제 매트릭스
    # matrix = [[''] * max_len for _ in range(5)]

    # # 매트릭스에 집어넣기
    # for row in range(5):
    #     for word in word_lst:
    #         for char in word:
    #             for col in range(len(word)):
    #                 matrix[row][col] = char
    
    # print(matrix)

    # ----- 매트릭스 폐기 -----#

		# 강사님 감사합니다.
		
    result = ''

    for col in range(max_len):
        for row in range(5):
            if col < len(word_lst[row]):
                result += word_lst[row][col]

    print(f'#{test_case} {result}')