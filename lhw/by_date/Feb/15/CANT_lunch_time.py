# SWEA - 2383
# 점심식사시간

# 입구까지 이동 시간
# 계단을 내려가는데 걸리는 시간 K

import sys
sys.stdin = open('input.txt')

def dfs(stair, people, K, time):




    pass

TC = int(input())
for test_case in range(1, TC+1):
    N = int(input())
    field = [list(map(int, input().split())) for _ in range(N)]

    # 계단 하나에는 3명까지만 올라갈 수 있음
    # 일단 DFS 같기는 한데
    # 계단 내려가고 있는걸 로테이트 활용해도 좋을 것 같고
    # 계단 입구까지 이동 시간이 다 비슷해야함
    # 최대값이 큰 놈부터 가까운 곳으로 이동하면 되나?

    # 계단 입구는 반드시 두개
    # 사람의 수는 1 ~ 10
    # 계단 길이는 2 ~ 10


    # 1. 계단 입구까지 이동 시간
    # - 최댓값이 큰 좌표부터 가까운 계단으로 이동
    # - 계단이 3명 꽉차면 다른 놈들은 다른 계단으로
    # - 계단에서 제일 가까운 사람이 그 계단으로 이동하고 다 내려가는데 걸리는 시간보다
    # - 최소거리가 더 긴 경우는 가장 가까운 사람도 가장 가까운 계단으로 이동

    # 그냥 계단마다 모든 사람이 다 내려가는데 걸리는 시간을 계산?
    # 좌표마다 딕셔너리로 계단 두개 모두의 소요시간을 기록하고
    # 가장 큰 값을 가지고 있는 사람을 작은 값의 계단으로 이동
    # 계단마다 리스트를 하나씩 할당하고 그 인덱스에 사람을 할당하자
    # 그럼 최대 최소를 구할 수 있고 최대가 최소 + K 보다 크면 둘 다 그 계단으로 넣을 수 있음

    people = []
    stair = []
    K = []
    for r in range(N):
        for c in range(N):
            if field[r][c] > 1:
                stair.append((r, c))
                K.append(field[r][c])
            if field[r][c] == 1:
                people.append((r, c))

    time_to_out = [[], []]
    for idx in range(2):
        sr, sc = stair[idx]
        for pr, pc in people:
            time_to_out[idx].append(abs(pr - sr) + abs(pc - sc) + K[idx])
    
    # print(time_to_out)
    assign = []
    for i in range(len(people)):
        if time_to_out[0][i] > time_to_out[1][i]:
            assign.append(stair[1])
        elif time_to_out[0][i] < time_to_out[1][i]:
            assign.append(stair[0])
    print(assign)
