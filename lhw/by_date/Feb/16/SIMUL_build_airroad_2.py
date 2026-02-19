# SWEA - 4014
# 활주로 건설
# 2회차

import sys
sys.stdin = open('input.txt')

# 경사로의 길이는 X, 높이는 1
# 높이가 2 이상 차이나면 불가

def counting(row):

    count = 1
    for i in range(1, N):
        if abs(row[i] - row[i-1]) >= 2:
            return 0

        if row[i] == row[i-1]:
            count += 1
        else:
            if row[i] > row[i-1]:  # 높아짐
                if count < X:
                    return 0
                else:
                    count = 1
            else:
                if count < 0:
                    return 0
                else:
                    count = -X+1
    if count < 0:
        return 0
    else:
        return 1


TC = int(input())
for test_case in range(1, TC+1):
    N, X = map(int, input().split())
    airport = [list(map(int, input().split())) for _ in range(N)]

    # 높이가 높아지면 이전의 카운팅이 X 이상이여야하고
    # 높이가 낮아지면 이후의 카운팅이 X 이상이어야한다.
    # 행이랑 열 한번씩만 보면 되는거긴 한데

    result = 0
    for row in airport:
        result += counting(row)


    for row in zip(*airport):
        result += counting(row)

    print(f'#{test_case} {result}')