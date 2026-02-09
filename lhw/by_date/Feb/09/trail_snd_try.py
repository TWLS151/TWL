import sys
sys.stdin = open('trail.txt')

# ------------- A ------------- #
# 깊이우선탐색, 재귀, 백트래킹

# --------- IM --------- #
# 백트래킹, 재귀, 델타, 완전탐색

directions = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]

def walk(row, col, road_len, cut_done):
    global max_len

    if max_len < road_len:
        max_len = road_len

    visited_area[row][col] = 1

    for i in range(4):
        dr, dc = directions[i]
        nr, nc = row + dr, col + dc

        if (
            0 <= nr < size and
            0 <= nc < size and
            not visited_area[nr][nc]
        ):
            if mountain[nr][nc] < mountain[row][col]:
                walk(nr, nc, road_len + 1, cut_done)  

            elif not cut_done and mountain[row][col] > mountain[nr][nc] - gongsa:
                original_height = mountain[nr][nc]
                mountain[nr][nc] = mountain[row][col] - 1

                walk(nr, nc, road_len + 1, True)

                mountain[nr][nc] = original_height

    visited_area[row][col] = 0


    pass

TC = int(input())

for test_case in range(1, TC+1):
    pass

    size, gongsa = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(size)]
    visited_area = [[0] * size for _ in range(size)]

    highest_height = 0
    for row in range(size):
        for col in range(size):
            if highest_height < mountain[row][col]:
                highest_height = mountain[row][col]

    max_len = 0
    for row in range(size):
        for col in range(size):
            if mountain[row][col] == highest_height:
                walk(row, col, 1, False)

    print(f'#{test_case} {max_len}')