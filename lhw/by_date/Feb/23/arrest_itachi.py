# SWEA - 1953
# 탈주범 검거

from collections import deque
import sys
sys.stdin = open('input.txt')

dirs = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]

pipes = {
    1: [0, 1, 2, 3],
    2: [0, 1],
    3: [2, 3],
    4: [0, 3],
    5: [1, 3],
    6: [1, 2],
    7: [0, 2]
}

oppo = {
    0: 1,
    1: 0,
    2: 3,
    3: 2
}

def CanIGoThere(nr, nc, field, dist, idx):

    if not (0 <= nr < N and 0 <= nc < M):  # 범위 먼저
        return False
    if not (field[nr][nc] != 0):  # 벽 안됨
        return False
    if dist[nr][nc] != -1:  # 갔던 곳은 다시 안감
        return False
    if oppo[idx] not in pipes[field[nr][nc]]:  # 지금 바라보고 있는 방향과 연결되어 있는지
        return False
    
    return True  # 다 통과하면 True 반환


def bfs(R, C, field):
    global N, M, L

    q = deque([(R, C)])  # 진입 위치
    dist = [[-1] * M for _ in range(N)]  # 방문처리 및 거리확인
    dist[R][C] = 1  # 진입 시간도 카운팅

    while q:  # BFS 시작
        row, col = q.popleft() 

        if dist[row][col] == L:  # 거리 == 시간이라 거리와 L 이 같아지면 넘김
            continue

        for idx in range(4):  # 네 방향
            if idx in pipes[field[row][col]]:  # 현재 위치한 파이프에 길이 뚫려있는지 확인
                dr, dc = dirs[idx]
                nr, nc = row+dr, col+dc

                if CanIGoThere(nr, nc, field, dist, idx):  # 이동 판단 함수
                    q.append((nr, nc))
                    dist[nr][nc] = dist[row][col] + 1

    count = 0
    for row in dist:  # 기록한 배열 순회하며 몇 칸인지 카운팅
        for val in row:
            if 0 <= val <= L:
                count += 1
    
    return count  # 반환

    pass


TC = int(input())
for test_case in range(1, TC+1):
    N, M, R, C, L = map(int, input().split())
    field = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{test_case} {bfs(R, C, field)}')

    
