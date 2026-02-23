# BOJ - 13460
# 구슬 탈출 2

from collections import deque

# import sys
# sys.stdin = open('input.txt')

dirs = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]


def roll(board, r, c, dr, dc):

    moved = 0
    while True:
        nr, nc = r + dr, c + dc
        if board[nr][nc] == '#':
            return r, c, moved, False
        r, c = nr, nc
        moved += 1
        if board[r][c] == 'O':
            return r, c, moved, True


def bfs():    
    N, M = map(int, input().split())
    board = [list(input()) for _ in range(N)]

    # 
    for r in range(N):
        for c in range(M):
            if board[r][c] == 'R':
                rr, rc = r, c
                board[r][c] = '.'
            if board[r][c] == 'B':
                br, bc = r, c
                board[r][c] = '.'
        
    visited = [[[[False]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]
    visited[rr][rc][br][bc] = True


    q = deque([(rr, rc, br, bc, 0)])

    while q:
        rr, rc, br, bc, depth = q.popleft()

        if depth == 10:
            continue

        for dr, dc in dirs:
            nrr, nrc, rmove, r_fell = roll(board, rr, rc, dr, dc)
            nbr, nbc, bmove, b_fell = roll(board, br, bc, dr, dc)

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
                q.append((nrr, nrc, nbr, nbc, depth+1))

    print(-1)



bfs()