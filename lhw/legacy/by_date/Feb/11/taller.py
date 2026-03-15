# BOJ - 2667
# 단지번호붙이기

import sys
# sys.stdin = open('taller.txt')
sys.setrecursionlimit(10**7)

directions = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]

def apartment(row, col):
    global count

    count += 1
    visited[row][col] = True

    for dr, dc in directions:
        nr, nc = row+dr, col+dc
        if (
            0<= nr < N and
            0<= nc < N and
            field[nr][nc] == '1' and
            not visited[nr][nc]
        ):
            apartment(nr, nc)
    
    pass


N = int(input())

field = [input() for _ in range(N)]
# print(field)
visited = [[False for _ in range(N)] for _ in range(N)]
# print(visited)
count_lst = []
for row in range(N):
    for col in range(N):
        if field[row][col] == '1' and not visited[row][col]:
            count = 0
            apartment(row, col)
            count_lst.append(count)

count_lst.sort()
print(len(count_lst))
for i in count_lst:
    print(i)
