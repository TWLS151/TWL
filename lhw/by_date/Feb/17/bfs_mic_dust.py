# BOJ - 17144
# 미세먼지 안녕!

# 공기 순환이 반대방향으로 설정되어있음.
import sys
sys.stdin = open('input.txt')

from collections import deque

# dirs = [
#     [(-1, 0), (0, 1), (1, 0), (0, -1)],
#     [(1, 0), (0, 1), (-1, 0), (0, -1)]
# ]  # dirs[0] 이 up 1 이 down

dirs = [
    [(0, 1), (-1, 0), (0, -1), (1, 0)],
    [(0, 1), (1, 0), (0, -1), (-1, 0)]
]  # dirs[0] 이 up 1 이 down

R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]


# BFS 로 공기청정기를 순환시키고
# 공기청정기 순환
dist = [[0]*C for _ in range(R)]

def bfs(lst):
    global dist, R, C

    for idx in range(2):
        r, c = lst[idx]
        q = deque([(r, c)])
        dist[r][c] = 1
        i = 0
        while q:
            pr, pc = q.popleft()
            # if (pr, pc) == (r, c) and i > 1:
            #     break
            dr, dc = dirs[idx][i]
            nr, nc = pr+dr, pc+dc
            if (nr, nc) == (r, c):
                break
            if 0<=nr<R and 0<=nc<C and dist[nr][nc] == 0:
                q.append((nr, nc))
                dist[nr][nc] = dist[pr][pc] + 1
            else:
                q.append((pr, pc))
                i += 1

    pass

# 미세먼지부터 구현해야겠네
# 좌표 필요한가? 필요하네
dust = []
machine = []
for r in range(R):
    for c in range(C):
        if room[r][c] > 0:
            dust.append((r, c))
        if room[r][c] == -1:
            machine.append((r, c))  # 0이 up 1이 down

bfs(machine)

for _ in range(T):

    # 먼지 확산
    # 방 안이고 공기청정기가 아니라면
    # 네 방향으로 확산한다.
    # 수 계산까지
    for r, c in dust:
        count = 0
        for dr, dc in dirs[0]:
            nr, nc = r+dr, c+dc
            if 0<=nr<R and 0<=nc<C and room[nr][nc] != -1:
                room[nr][nc] += room[r][c]//5
                count += 1
                if (nr, nc) not in dust:
                    dust.append((nr, nc))
        room[r][c] -= room[r][c]//5 * count


    # # 먼지 이동
    # for r in range(R):
    #     for c in range(C):
    for pr, pc in machine:
        r, c = pr, pc
        for dr, dc in dirs[0]:
            nr, nc = r+dr, c+dc
            if 0<=nr<R and 0<=nc<C:
                if room[nr][nc] != -1 and dist[r][c] != 0 and dist[r][c] == dist[nr][nc] - 1:
                    if room[r][c] == -1:
                        room[nr][nc] = 0
                    else:
                        room[r][c] = room[nr][nc]

total = 0
for r in range(R):
    for c in range(C):
        if room[r][c] > 0:
            total += room[r][c]

print(total)

                