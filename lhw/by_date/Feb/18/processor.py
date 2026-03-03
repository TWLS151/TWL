# SWEA - 1767
# 프로세서 연결하기

# 필드에 코어와 전선
# 전선은 교차하면 안되고 오직 직선
# 가장자리는 전류가 흐름
# 최대한 많은 코어에 전원을 연결하고
# 전선 길이의 합의 최소

# DFS로 하고 후보군 리스트 만들고 [연결 수, 전선 길이]로 모든 경우의 수 넣고
# 정렬해서 반환

import sys
sys.stdin = open('input.txt')


dirs = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]

def can_lay(field, N, r, c, d):

    dr, dc = dirs[d]
    nr, nc = r+dr, c+dc
    path = []
    while 0 <= nr < N and 0 <= nc < N:
        if field[nr][nc] != 0:
            return 0, []
        path.append((nr, nc))
        nr+=dr
        nc+=dc

    return len(path), path


def dfs(idx, connected, wire_len):
    global best_connected, best_len, N, field, core_lst

    # 가지치기
    # 이미 전선 수가 최소보다 많아지면 잘라내도 됨
    if connected == best_connected and wire_len >= best_len:
        return

    # 기저조건
    # 모든 코어를 다 확인하면 종료 == for문으로 처리
    remain = len(core_lst) - idx
    if connected + remain < best_connected:
        return

    if idx == len(core_lst):
        if connected > best_connected:
            best_connected = connected
            best_len = wire_len
        elif connected == best_connected:
            best_len = min(best_len, wire_len)
        return

    # 분기
    # 코어를 연결 하냐 안하냐
    # 연결해도 어느 방향으로 연결하냐

    r, c = core_lst[idx]

    laid_any = False
    for d in range(4):
        length, path = can_lay(field, N, r, c, d)
        if length == 0:
            continue
        laid_any = True

        for pr, pc in path:
            field[pr][pc] = 2

        dfs(idx+1, connected+1, wire_len+length)

        for pr, pc in path:
            field[pr][pc] = 0

    dfs(idx+1, connected, wire_len)


    pass


TC = int(input())
for test_case in range(1, TC+1):
    N = int(input())
    field = []
    core = []
    for r in range(N):
        row = list(map(int, input().split()))
        for c in range(1, N-1):
            if r == 0 or r == N-1:
                break
            if row[c] == 1:
                core.append((r, c))
        field.append(row)

    

    best_connected = -1
    best_len = 10**9

    dfs(0, 0, 0)

    print(f'#{test_case} {best_len}')

    # 마지막에 개수 출력할 때 가장자리 수 더해야함