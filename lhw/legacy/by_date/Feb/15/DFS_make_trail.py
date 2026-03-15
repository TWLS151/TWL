# SWEA - 1949
# 등산로 조성
# 2회차

# 가장 높은 곳에서 시작
# 반드시 높은 곳에서 낮은 곳으로
# 딱 한 곳 k 깊이만큼 깎을 수 있다
# 가장 긴 등산로를 찾아라

import sys
sys.stdin = open('input.txt')

# 델타 생성
dirs = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]


def trail(r, c, used_cut):

    visited[r][c] = True
    
    count = 1

    # 이미 갈 수 있는 방향은 정해져있다.
    for dr, dc in dirs:
        nr, nc = r+dr, c+dc
        if 0<=nr<N and 0<=nc<N and not visited[nr][nc]:
            if mountain[nr][nc] < mountain[r][c]:
                count = max(count, 1 + trail(nr,nc, used_cut))

            elif used_cut == 0:
                gongsa = mountain[nr][nc] - mountain[r][c] + 1

                if 1<= gongsa <= K:
                    origin = mountain[nr][nc]
                    mountain[nr][nc] = mountain[r][c] - 1
                    count = max(count, 1 + trail(nr,nc,1))
                    mountain[nr][nc] = origin

    visited[r][c] = False

    return count
    pass

TC = int(input())
for test_case in range(1, TC+1):
    N, K = map(int, input().split())
    mountain = [list(map(int ,input().split())) for _ in range(N)]

    # 가장 높은 곳부터 찾아야한다.
    highest = 0
    for i in range(N):
        for j in range(N):
            highest = max(highest, mountain[i][j])
    
    visited = [[False] * N for _ in range(N)]

    # 공사하기 전에 가장 긴 등산로를 찾아야한다.
    result = 0
    for row in range(N):
        for col in range(N):
            if mountain[row][col] == highest:
                result = max(result, trail(row, col, 0))
            # 가장 긴 등산로를 찾아야함.
            # 시작지점, 지도
    
    print(f'#{test_case} {result}')