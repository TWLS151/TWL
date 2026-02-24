from collections import deque

dirs = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]

def roll(r, c, dr, dc, board):

    moved = 0
    while True:
        nr, nc = r+dr, c+dc
        if board[nr][nc] == '#':
            return r, c, moved, False
        r, c = nr, nc
        moved += 1
        if board[r][c] == 'O':
            return r, c, moved, True


    pass


def bfs():

    N, M = map(int, input().split())
    board = [list(input()) for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if board[r][c] == 'R':
                rr, rc = r, c
                board[r][c] = '.'
            if board[r][c] == 'B':
                br, bc = r, c
                board[r][c] = '.'
    
    visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
    visited[rr][rc][br][bc] = True

    q = deque([(rr, rc, br, bc, 0)])

    while q:
        rr, rc, br, bc, depth = q.popleft()

        if depth == 10:
            continue

        for dr, dc in dirs:
            nrr, nrc, rmove, r_fell = roll(rr, rc, dr, dc, board)
            nbr, nbc, bmove, b_fell = roll(br, bc, dr, dc, board)

# 1. 10번 안에 끝내야한다.
# 2. 파란공은 나오면 안된다.
# 3. 빨강과 파랑은 같은 위치에 있을 수 없다.

        if b_fell:
            continue

        if r_fell:
            print(depth + 1)
            return
        
        if (nrr, nrc) == (nbr, nbc):
            if rmove > bmove:
                nrr -= dr
                nrc -= dc
            else:
                nbr -= dr
                nbc -= dc

        if (nrr, nrc, nbr, nbc) == (rr, rc, br, bc):
            continue

        if not visited[nrr][nrc][nbr][nbc]:
            visited[nrr][nrc][nbr][nbc] = True
            q.append((nrr, nrc, nbr, nbc, depth + 1))
    print(-1)


bfs()