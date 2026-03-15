# SWEA - 1953
# 탈주범 검거
# 2회차
# 1회차보다 조금 더 맘에 드는 방식

# 시간당 1의 거리 이동
# 터널 구조물 7가지
# 탈주범이 위치할 수 있는 장소의 개수

import sys
from collections import deque

sys.stdin = open('input.txt')

directions = [
    0, (-1, 0), (1, 0), (0, -1), (0, 1)
]

things = {
    1: {1, 2, 3, 4},
    2: {1, 2},
    3: {3, 4},
    4: {1, 4},
    5: {2, 4},
    6: {2, 3},
    7: {1, 3}
}
oppo = {1: 2, 2: 1, 3: 4, 4: 3}

def canigothere(r, c, nr, nc, idx):
    global N, M, R, C, L, tizu, visited

    if not (0 <= nr < N and 0<= nc < M):
        return False
    
    if tizu[nr][nc] == 0:
        return False
    
    if visited[nr][nc]:
        return False
    
    if oppo[idx] not in things[tizu[nr][nc]]:
        return False
    
    return True


def radar(r, c, time):
    global N, M, R, C, L, tizu, visited
    # 시작위치
    # 시간
    q = deque()
    q.append((r, c, time))
    visited[r][c] = True
    count = 1
    while q:
        pr, pc, time = q.popleft()

        if time == L:
            continue

        for idx in things[tizu[pr][pc]]:
            dr, dc = directions[idx]
            nr, nc = pr+dr, pc+dc
            if canigothere(pr, pc, nr, nc, idx):
                visited[nr][nc] = True
                q.append((nr, nc, time + 1))
                count += 1
    return count
    

TC = int(input())
for test_case in range(1, TC+1):
    N, M, R, C, L = map(int, input().split())
    tizu = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    print(f'#{test_case} {radar(R, C, 1)}')