# SWEA - 1979
# 어디에 단어가 들어갈 수 있을까

import sys
sys.stdin = open('where_is_my_sheet.txt')

TC = int(input())

def findK(matrix, length):
    pass
    result = 0
    for row in matrix:
        count = 0
        for num in row:
            if num == '1':
                count += 1
            else:
                if count == length:
                    result += 1
                count = 0
        if count == length:
            result += 1
            
    return result


for test_case in range(1, TC+1):
    size, length = map(int, input().split())
    board = [input().split() for _ in range(size)]
    pass

# length 가 딱 들어맞는 위치가 몇 개인지 찾아라
# 1이 length 만큼 연속되는 구간을 찾자
# 가로 세로만 보면 되는 문제

    result = findK(board, length)

    # 이 문제에 전치는 위험하다
    # transed_board = list(map(list, zip(*board)))

    # 반시계 방향으로 돌리자
    transed_board = [[0] * size for _ in range(size)]

    for i in range(size):
        for j in range(size):
            transed_board[i][j] = board[j][size - 1 - i]

    result += findK(transed_board, length)

    print(f'#{test_case} {result}')








# ----------------------------------------- #

    # print(f'#{test_case} {count}')



    #     # 문자열로 바꾸고 '1'*length 해서 그걸 찾으면 되겠는데
    # # 그럼 인풋부터 문자열로 받아야겠네
    # # 세로는 전치해서 가로 다시 보고

    # count = 0
    # # 문자열 바꿔서 확인하기
    # for row in board:
    #     string = ''.join(row).replace('1'*length, 'k')
    #     # print(string)
    #     # if '1k' not in string and 'k1' not in string and '1k1' not in string and 'kk' not in string and 'k' in string:
    #     count += string.count('k0')
    #     count += string.count('0k')
    #     count -= string.count('0k0')
    #     count -= string.count('1k')
    #     count -= string.count('k1')
    #     count += string.count('1k1')

    # # 이 문제에 전치는 위험하다
    # # transed_board = list(map(list, zip(*board)))

    # # 반시계 방향으로 돌리자
    # transed_board = [[0] * size for _ in range(size)]

    # for i in range(size):
    #     for j in range(size):
    #         transed_board[i][j] = board[j][size - 1 - i]

    # for row in transed_board:
    #     string = ''.join(row).replace('1'*length, 'k')
    #     # if '1k' not in string and 'k1' not in string and '1k1' not in string and 'kk' not in string and 'k' in string:
    #     count += string.count('k0')
    #     count += string.count('0k')
    #     count -= string.count('0k0')
    #     count -= string.count('1k')
    #     count -= string.count('k1')
    #     count += string.count('1k1')