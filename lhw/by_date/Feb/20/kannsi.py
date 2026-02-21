# BOJ - 15683
# 감시

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(N)]

dirs = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]

rotate = {
    1: [[0], [1], [2], [3]],
    2: [(0, 1), (2, 3)],
    3: [(0, 3), (3, 1), (1, 2), (0, 2)],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[0, 1, 2, 3]]
}

def init():
    obj = []
    ans = 0
    for i in range(N):
        for j in range(M):
            if field[i][j] != 6 and field[i][j] != 0:
                obj.append((field[i][j], i, j))
            if field[i][j] == 0:
                ans += 1
    return obj, ans

cctv, answer = init()


def check(r, c):
    return 0 <= r < N and 0 <= c < M


def move(r, c, d, space_copy):

    for d in dirs:
        nr, nc = r, c

        while True:
            nr += d[0]
            nc += d[1]

            if not check(nr, nc) or space_copy[nr][nc] == 6:
                break
            if space_copy[nr][nc] != 0:
                continue
            space_copy[nr][nc] = '#'


def zero_cnt(space_copy):
    global answer
    cnt = 0
    for i in space_copy:
        cnt += i.count(0)
    answer = min(answer, cnt)


def dfs(level, field):

    space_copy = [[j for j in field[i]] for i in range(N)]

    if level == len(cctv):
        zero_cnt(space_copy)
        return
    
    number, r, c = cctv[level]

    for d in rotate[number]:
        move(r, c, d, space_copy)
        dfs(level + 1, space_copy)
        space_copy = [[j for j in field[i]] for i in range(N)]

dfs(0, field)
print(answer)