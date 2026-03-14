# SWEA - 2112
# 보호 필름
# 2회차

import sys
sys.stdin = open('input.txt')

# sys.setrecursionlimit = 10**7

def counting():

    for col in range(W):
        count = 1
        ok = False
        for row in range(1, D):
            if film[row][col] == film[row-1][col]:
                count += 1
            else:
                count = 1
            if count >= K:  # 다음행으로
                ok = True
                break
        if not ok:  # 다 봤는데 안됐으면
            return False  # 실패
    return True

def dfs(r, t):
    global D, W, K, film, time
    # 기저조건
    # 카운트가 모두 다 통과했을 때

    if t > time:
        return

    if r == D:
        if counting():
            time = min(time, t)
        return
    
    # 할 일
    # 지금 위치에 약을 뿌린거 안뿌린거 두개 분기탐색

    if 0<=r+1<=D:

        origin = film[r][:]
        # 안뿌린거
        dfs(r+1, t)
        # 뿌린거
        film[r] = [0] * W
        dfs(r+1, t+1)

        film[r] = [1] * W
        dfs(r+1, t+1)

        film[r] = origin


TC = int(input())
for test_case in range(1, TC+1):
    D, W, K = map(int, input().split())
    film = [list(map(int, input().split())) for _ in range(D)]

    # K 개 연속으로 같은 특성이 있어야함
    # 카운팅 하다가 달라지면 카운팅 초기화
    # 약품 넣을 때마다 카운팅 새로 해야겠네
    # 모두 다 통과해야함
    
    

    # K 가 1이면 그냥 항상 통과
    if K == 1:
        print(f'#{test_case} 0')
        continue

    time = K

    dfs(0, 0)

    # 열은 고정하고 행만 탐색해야함
    # 약을 어디 뿌릴건데?
    print(f'#{test_case} {time}')