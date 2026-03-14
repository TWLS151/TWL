# SWEA - 4875
# 미로

# import sys
# sys.stdin = open('maze.txt')

directions = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]

def findRoad(row, col):
    global result
    
    visited[row][col] = True
    
    if maze[row][col] == '3':
        result = 1

    for dirs in directions:
        dr, dc = dirs
        nr, nc = row+dr, col+dc
        
        if 0 <= nr < size and 0 <= nc < size:
            if maze[nr][nc] != '1' and not visited[nr][nc]:
                findRoad(nr, nc)
    pass

TC = int(input())

for test_case in range(1, TC+1):
    size = int(input())
    maze = [list(map(str, input())) for _ in range(size)]

    visited = [[False for _ in range(size)] for _ in range(size)]

    result = 0 
    for row in range(size):
        for col in range(size):
            if maze[row][col] == '2':
                findRoad(row, col)
                pass

    print(f'#{test_case} {result}')
