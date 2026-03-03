# IM
# 짜르 봄바
# TTP: 12'39"

import sys
sys.stdin = open('ssar_bomb.txt')

TC = int(input())

directions = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]

def effect(row, col, dis):
    pass
    total = field[row][col]
    for distance in range(1, dis):
        for idx in range(4):
            dr, dc = directions[idx]
            nr, nc = row + dr * distance, col + dc * distance
            if (
                0 <= nr < len(field) and
                0 <= nc < len(field[0])
            ):
                total += field[nr][nc]            
    return total




for test_case in range(1, TC+1):
    height, width = map(int, input().split())
    field = [list(map(int, input().split())) for _ in range(height)]

    total = []
    for row in range(height):
        for col in range(width):
            dis = field[row][col]
            total.append(effect(row, col, dis + 1))

    print(f'#{test_case} {max(total)}')