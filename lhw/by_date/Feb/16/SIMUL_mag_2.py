# SWEA - 4013
# 특이한 자석
# 2회차

# 하나의 자석이 회전될 때 붙어있는 자석은
# 서로 붙어있는 날의 자성과 다를 경우에만 반대방향으로 회전

# 시계방향이 1, 반시계는 -1

import sys
sys.stdin = open('input.txt')

directions = [0, -1, 1]

TC = int(input())
for test_case in range(1, TC+1):
    K = int(input())
    topnis = [0] + [list(map(int, input().split())) for _ in range(4)]

    score = 0
    # 톱니를 회전시키지 말고 포인터를 움직여볼까
    pointer = [0] * 5
    for _ in range(K):
        n, d = map(int, input().split())
        # d == 1 이면 톱니는 시계, 포인터는 반시계
        # d == -1 이면 톱니는 반시계, 포인터는 시계

        pointer[n] += directions[d]

        left = n
        # 왼쪽 오른쪽으로 확산해야함
        while 0 < left-1:  # 왼쪽 톱니가 있고
            if topnis[left][6] != topnis[left-1][2]:  # 둘의 극이 서로 다르면
                pointer[left-1] += d  # 반대방향으로 회전 // 포인터는 같은 방향으로 회전
            left -= 1

        right = n
        while right+1 < 5:  # 오른쪽 톱니가 있으면
            if topnis[right][2] != topnis[right+1][6]:
                pointer[right+1] += d
            right += 1

        # # 이제 포인터를 정해야하는데
        # # 포인터를 움직이면 상태가 하나 추가되긴 하네
        # pointer = [0] * 5

    # 1단 idx == 0 에서 점수부터
    # if topnis[n][0] == 1:
    #      score = 2**(n-1)
    for i in range(1, 5):
        if topnis[i][pointer[i]%8] == 1:
            score += 2**(i-1)

    print(score)