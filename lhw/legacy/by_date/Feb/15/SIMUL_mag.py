# SWEA - 4013
# 특이한 자석

import sys
from collections import deque
sys.stdin = open('input.txt')

# DP?
# 하나의 자석이 한 칸 회전될 때 붙어 있는 자석은
# 서로 붙어있는 날의 자성과 다를 경우에만 인력에 의해 반대 방향으로 한 칸 회전
# 점수 조건 네가지

######
# 4개 자석의 자성 정보와 자석을 한 칸씩 k번 회전 시키려고 할 때
# k번 자석을 회전시킨 후 획득하는 점수의 총 합
# DP인가봐
# DFS?

def isitpossible(target, num1, num2):

    if num1 > num2:  # 왼쪽으로 가는거
        if target[6] != topni[num2][2]:  # 다르면 돌린다
            return True
        return False

    else:
        if target[2] != topni[num2][6]:  # 다르면 돌린다
            return True
        return False

    # 2번 인덱스와 6번 인덱스의 관계만 보면 됨
    # 왼쪽으로 가는거면 오리진의 6번과 어나더의 2번
    # 오른쪽으로 가는거면 오리진의 2번과 어나더의 6번


oppo = [0, -1, 1]  # 인덱스로 반대방향 설정

def dfs(num, d):
    global score

    done[num] = True

    target = deque(topni[num])
    # target.rotate(d)
    
    # 돌리는것 까지는 했다.
    # 돌린걸 다른 톱니한테도 영향을 줘야해

    if num-1 >= 1 and not done[num-1] and isitpossible(target, num, num-1):
        dfs(num-1, oppo[d])  # 왼쪽에 있는 톱니 돌린다.

    if num+1 <= 4 and not done[num+1] and isitpossible(target, num, num+1):
        dfs(num+1, oppo[d])  # 오른쪽 톱니 돌린다.

    target.rotate(d)

    topni[num] = list(target)

    done[num] = False

    # if target[0] == 1:
    #     score += 2 ** (num-1)

    # 구현은 했다. 이제 조건에 맞춰 돌아가는걸 만들어야하네
    # if 문에 조건을 추가해야겠지
    # 함수 하나 파자


TC = int(input())
for test_case in range(1, TC+1):
    K = int(input())
    topni = [list(map(int, input().split())) for _ in range(4)]
    order = [list(map(int, input().split())) for _ in range(K)]

    topni.insert(0,0)
    order.insert(0,0)

    # order[k][0] = 톱니 번호 // [k][1] = 회전 방향
    # 톱니의 자성 정보는 화살표 위치부터 시계방향으로 주어진다.

    # 지정된 톱니를 돌리면 다른 톱니들도 알아서 돌아가는 구조
    # 그냥 시뮬레이션?
    # 로테이션 돌리면 편하긴 하겠는데

    # 1번 톱니를 회전 시키면
    # 2번 톱니에 영향이 가고
    # 데크 써서 BFS?

    done = [False for _ in range(5)]

    score = 0
    for i in range(1, K + 1):
        dfs(order[i][0], order[i][1])  # 번호랑 방향 인자로
        
    for j in range(1, 5):
        if topni[j][0] == 1:
            score += 2 ** (j - 1)
    
    print(f'#{test_case} {score}')
