'''
그래프 탐색 실전 - 섬 찾기 문제입니다.
'''

import sys
# sys.stdin = open('./graph_prac/input.txt', 'r')
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())

arr = [list(map(int, (list(input())))) for _ in range(N)]

# 1. 탐색에 필요한 요소 구성

visited = [[False]*N for _ in range(M)] # 방문처리 행렬
d = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1)] # 아래로 5방향을 탐색하기 위함
island = 0  # 섬 개수
path = []

def in_range(x, y): # 범위 검색 함수
    return 0 <= x < y

def dfs_recursive(r, c):

    if visited[r][c] == True: # 탐색 종료 3 : 방문했던 곳일 때
        return

    # 1. 해당 지점 방문처리
    visited[r][c] = True
    path.append((r, c))

    for dr, dc in d: # 2. 아래 5방향에 대해 DFS
        nr = r + dr
        nc = c + dc

        if in_range(nr, N) and in_range(nc, M) and arr[nr][nc] == 1: # 만약 범위 내에 있고 땅이 있다면
            dfs_recursive(nr, nc)


for i in range(N):
    for j in range(M):

        if arr[i][j] == 1 and not visited[i][j]: # 섬의 새로운 땅을 발견하면 탐색 시작
            
            island += 1 # 섬 개수 추가
            dfs_recursive(i, j) # 재귀 시작


print(island)
print(path)