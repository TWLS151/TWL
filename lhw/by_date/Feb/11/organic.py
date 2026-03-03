# BOJ - 1012
# 유기농 배추

import sys
# sys.stdin = open('organic.txt')
sys.setrecursionlimit(10**7)

directions = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]

def findWarm(row, col):

    visited[row][col] = True

    for dr, dc in directions:
        nr, nc = row+dr, col+dc
        if 0<= nr < height and 0<= nc < width:
            if farm[nr][nc] != 0 and not visited[nr][nc]:
                findWarm(nr, nc)


TC = int(input())

for test_case in range(1, TC+1):
    width, height, K = map(int, input().split())
    farm = [[0 for _ in range(width)] for _ in range(height)]
    visited = [[False for _ in range(width)] for _ in range(height)]
    
    for _ in range(K):
        col, row = map(int, input().split())
        farm[row][col] = 1
    
    count = 0
    for row in range(height):
        for col in range(width):
            if farm[row][col] == 1 and not visited[row][col]:
                findWarm(row, col)
                count += 1

    print(count)