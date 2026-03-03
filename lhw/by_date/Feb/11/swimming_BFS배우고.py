# SWEA - 4193
# 수영대회 결승전

import sys

sys.setrecursionlimit(10 ** 7)
sys.stdin = open('swimming.txt')


directions = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]

def swim(row, col):

    if (row, col) == (C, D):
        return 0
    
    visited[row][col] = True
    distance = 1

    position = (row, col)
    pr, pc = position
    best = 10 ** 5
    for dr, dc in directions:
        nr, nc = pr+dr, pc+dc
        if 0 <= nr < N and 0 <= nc < N and marine[nr][nc] == 0 and not visited[nr][nc]:

            marine[row][col] = 0
            distance += swim(nr, nc)
    
    best = min(best , distance)
    visited[row][col] = False

    return best
    pass



TC = int(input())

for test_case in range(1, TC+1):
    N = int(input())
    marine = [list(map(int, input().split())) for _ in range(N)]
    A, B = map(int, input().split())
    C, D = map(int, input().split())

    visited = [[False for _ in range(N)] for _ in range(N)]

    # 섬은 1, 소용돌이 2
    # 소용돌이는 2초 있고 1초 없고 사이클

    max_dis = swim(A, B)
    print(max_dis)
    
    # time = 0
    # tornado = time % 3 - 2
    # for row in range(N):
    #     for col in range(N):
    #         if marine[row][col] == 2:
    #             marine[row][col] = tornado

    # for i in range(3):
    #     time = i
    #     swim(A, B)
    
