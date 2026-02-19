# BOJ - 16236
# 아기 상어

# 작은 물고기를 만나면 바로바로 먹는 건 구현을 했는데
# 여러마리일 경우 후보군을 만들어서 관리하는 건 실패했다.

import sys
sys.stdin = open('input.txt')

from collections import deque

dirs = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]

def bfs(sr, sc, s, e, t):  # 시간을 상태로 유지 할 필요가 있을까?
    q = deque([(sr, sc, s, e, t)])
    dist = [[-1]*N for _ in range(N)]
    dist[sr][sc] = 0
    smalls = []
    while q:  # dist 매번 초기화해야할 듯?
        r, c, s, e, t = q.popleft()

        
        if field[r][c] != 0 and field[r][c] < s:
            # dist[r][c] # 이게 지금 제일 처음 만난 작은 물고기까지의 거리잖아?
            # 리스트 하나 만들어야겠다.

            # 일단 먹고 여러마리는 나중에 생각하자.
            field[r][c] = 9
            field[sr][sc] = 0
            t += dist[r][c]
            e += 1
            if e == s:
                s += 1
                e = 0
            dist = [[-1]*N for _ in range(N)]
            dist[r][c] = 0
            q = deque([(r, c, s, e, t)])
            r, c, s, e, t = q.popleft()

        # smalls = []

        for dr, dc in dirs:
            nr, nc = r+dr, c+dc

            if 0 <= nr < N and 0 <= nc < N:
                if field[nr][nc] <= s and dist[nr][nc] == -1:
                    q.append((nr, nc, s, e, t))
                    dist[nr][nc] = dist[r][c] + 1
                    if field[nr][nc] != 0:
                        smalls.append((dist[nr][nc], nr, nc))
                        smalls.sort(key= lambda x: (x[0], x[1], x[2]))

    return t
    # 방향 필요한가? 직접 이동할 필요가 없긴한데
    # bfs 로 물고기 거리만 잡고
    # 

N = int(input())
field = [list(map(int, input().split())) for _ in range(N)]

# r, c, 크기, 먹은 물고기, 시간
# 크기 == 먹은 물고기가 되면 크기 +1, 먹물 0
# 거리가 같으면 가장 위, 가장 왼쪽 순서
# 시간도 재야하니까 상태 추가
# dist로 물고기 사이 거리

# 상어 찾기

for r in range(N):
    for c in range(N):
        if field[r][c] == 9:
            shark = (r, c)  # 좌표, 크기, 먹물, 시간

r, c = shark
result = bfs(r, c, 2, 0, 0)

print(result)