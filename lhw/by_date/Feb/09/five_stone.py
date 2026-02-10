# SWEA - 11315
# 오목 판정
# TTP: 23'

# import sys
# sys.stdin = open('five_stone.txt')

directions = [
    (-1, 0), (1, 0), (0, -1), (0, 1),
    (-1, -1), (-1, 1), (1, -1), (1, 1)
]
# 완전탐색하면 같은 걸 두번 카운팅 할 수도 있는데
# 이 문제는 그냥 여부만 판단하는거라 상관 없겠다.
# 개수를 세라고하면 방향을 4개만 확인하면 되려나? 나중에 해보자
def isItFive(row, col):

    result = 0
    for dr, dc in directions:
        nr, nc = row + dr, col + dc
        # 너 자신도 세야지 이자식아
        count = 1
        while 0 <= nr < size and 0 <= nc < size and board[nr][nc] == 'o':
            nr, nc = nr + dr, nc + dc
            count += 1
            if count == 5:
                break
        if count == 5:
            result = 1
            break

    return result

TC = int(input())

for test_case in range(1, TC+1):
    size = int(input())

    board = [input() for _ in range(size)]

    stop = False
    # 돌을 찾아야겠네.
    for row in range(size):
        if not stop:
            for col in range(size):
                if board[row][col] == 'o':
                    if isItFive(row, col) == 1:
                        stop = True
                        break
    if stop == True:
        print(f'#{test_case} YES')
    else:
        print(f'#{test_case} NO')