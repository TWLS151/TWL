import sys
sys.stdin = open('input.txt')

from collections import deque

input = sys.stdin.readline
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def apply_actions(state, cell):
    # state: (s1, s2, s3, s4) 각 0/1/2
    s = list(state)

    if 1 <= cell <= 4:          # 몬스터 i
        i = cell - 1
        if s[i] == 0:
            s[i] = 1            # 포획
    elif -4 <= cell <= -1:      # 손님 -i
        i = (-cell) - 1
        if s[i] == 1:
            s[i] = 2            # 전달

    return tuple(s)

def solve():
    N = int(input().strip())
    grid = [list(map(int, input().split())) for _ in range(N)]

    target = (2, 2, 2, 2)

    start_state = apply_actions((0, 0, 0, 0), grid[0][0])

    # dist[r][c]는 dict로: {state: distance}
    dist = [[dict() for _ in range(N)] for _ in range(N)]
    q = deque([(0, 0, start_state)])
    dist[0][0][start_state] = 0

    while q:
        r, c, state = q.popleft()
        d = dist[r][c][state]

        if state == target:
            print(d)
            return

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N:
                nstate = apply_actions(state, grid[nr][nc])
                if nstate not in dist[nr][nc]:
                    dist[nr][nc][nstate] = d + 1
                    q.append((nr, nc, nstate))

if __name__ == "__main__":
    solve()
