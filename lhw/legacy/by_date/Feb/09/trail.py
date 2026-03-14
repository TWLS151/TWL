# SWEA - 1949
# 등산로 조성
# Fail: 102'25"

# 크기 N 의 필드에서 최대한 긴 등산로
# 필드의 각 좌표에는 숫자가 있고 이 숫자는 지형의 높이를 나타낸다.

import sys
sys.stdin = open('trail.txt')

TC = int(input())

def nextWay(row, col, mountain):
    size = len(mountain)
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # 인자로 들어온 현재 포지션
    position = (row, col)
    # 포지션 저장
    pr, pc = position
    count = 0
    for dr, dc in dirs:
        nr, nc = pr + dr, pc + dc
        if (
            0 <= nr < size and
            0 <= nc < size and
            mountain[nr][nc] < mountain[pr][pc]
        ):
            count = max(count, nextWay(nr, nc, mountain))

    return count + 1


def makeTrail(mountain, highest_height):
    pass
    max_count = 0
    size = len(mountain)
    for row in range(size):
        for col in range(size):
            if mountain[row][col] == highest_height:
                count = nextWay(row, col, mountain)
                if max_count < count:
                    max_count = count
    return max_count

for test_case in range(1, TC+1):
    size, gongsa = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(size)]

    # highest
    highest_height = 0
    for row in range(size):
        for col in range(size):
            if highest_height < mountain[row][col]:
                highest_height = mountain[row][col]

    max_count = 0
    count = makeTrail(mountain, highest_height)
    if max_count < count:
        max_count = count


    # 이제 그냥 하나씩 1 깎고 돌리면 되는거 아닌가?
    # 매트릭스 하나 더 해야겠네
    
    gongsaed_max_count = 0
    for row in range(size):
        for col in range(size):
            backup = mountain[row][col]
            gongsaed_height = backup - 1
            mountain[row][col] = gongsaed_height

            # 깎인 산의 highest
            gongsaed_highest = 0
            for i in range(size):
                for j in range(size):
                    if mountain[i][j] > gongsaed_highest:
                        gongsaed_highest = mountain[i][j]
            gongsa_count = makeTrail(mountain, gongsaed_highest)
            if gongsaed_max_count < gongsa_count:
                gongsaed_max_count = gongsa_count

            mountain[row][col] = backup

    if max_count < gongsaed_max_count:
        max_count = gongsaed_max_count

    print(f'#{test_case} {max_count}')

