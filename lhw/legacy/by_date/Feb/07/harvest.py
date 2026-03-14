# SWEA - 2805
# 농작물 수확하기

import sys
sys.stdin = open('harvest.txt')

TC = int(input())

for test_case in range(1, TC+1):
    pass
    size = int(input())
    farm = [[int(i) for i in input()] for _ in range(size)]

    # 항상 홀수
    # ㅎ항상 딱 맞는 마름모
    # 가운데서 퍼져나가자
    
    # 중앙 좌표
    mid = size//2
    # farm[mid - '한칸씩'][mid: '양옆에 한칸씩 줄면']
    # for i in range(mid):
    #     for j in range(i, mid-i):
    #         farm[mid-i][j]

    total_crop = 0
    # # 위 아래 한 번에 가자
    # for row in range(mid):
    #     for col in range(mid):
    #         # 중앙 행 다 더하고
    #         total_crop += sum(farm[mid])
    #         total_crop += sum(farm[mid])

    for updown in range(mid+1):
        for side in range(updown, size-updown):
            total_crop += farm[mid + updown][side]
            total_crop += farm[mid - updown][side]
    total_crop -= sum(farm[mid])

    print(f'#{test_case} {total_crop}')