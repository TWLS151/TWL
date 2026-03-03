# SWEA - 1861
# 정사각형 방

import sys

# sys.stdin = open('room.txt')
sys.setrecursionlimit(10**7)
directions = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]

def findRoom(row, col):
    
    if dp[row][col] != 0:
        return dp[row][col]

    count = 1

    for dr, dc in directions:
        nr, nc = row+dr, col+dc

        if 0 <= nr < N and 0 <= nc < N  and rooms[nr][nc] == rooms[row][col] + 1:
            
            count = max(count, 1+findRoom(nr, nc))
    dp[row][col] = count
    return count

TC = int(input())

for test_case in range(1, TC+1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0 for _ in range(N)] for _ in range(N)]


    best_len = 0
    best_start = 10**9
    for row in range(N):
        for col in range(N):
            count = findRoom(row, col)
            start = rooms[row][col]
            if best_len < count or (count == best_len and start < best_start):
                best_len = count
                best_start = start

    print(f'#{test_case} {best_start} {best_len}')