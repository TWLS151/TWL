# 섬 찾기

# 일단 DFS
# 배열 받

# import sys
# sys.stdin = open('find_island.txt')

directions = [
    (-1, 0), (1, 0), (0, -1), (0, 1),
    (-1, -1), (-1, 1), (1, 1), (1, -1)
]

def findOne(row, col):

    visited_island[row][col] = True

    for idx in directions:
        dr, dc = idx
        nr, nc = row + dr, col + dc

        if 0 <= nr < len(field) and 0 <= nc < len(field):
            if field[nr][nc] == 1 and not visited_island[nr][nc]:
                findOne(nr, nc)

    pass


# TC = int(input())

for test_Case in range(1, 1+1):
    height, width = map(int, input().split())
    field = [list(map(int, input())) for _ in range(height)]

    visited_island = [[False for _ in range(width)] for _ in range(height)]

    # print(visited_island)

    count = 0

    for row in range(height):
        
        for col in range(width):

            if field[row][col] == 1 and not visited_island[row][col]:
                count += 1
                findOne(row, col)
                

print(count)