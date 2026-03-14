# BOJ - 13460
# 구슬 탈출 2
# SSSW 기출 달리기
# import sys
# sys.stdin = open('input.txt')

from collections import deque

dirs = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]

def moving(r, c, dr, dc, board):

    move = 0
    while True:
        nr, nc = r+dr, c+dc
        if board[nr][nc] == '#':
            return r, c, move, False
        move += 1
        r, c = nr, nc
        if board[nr][nc] == 'O':
            return nr, nc, move, True



def bfs():
    # [1] 파란 구슬이 구멍에 들어가면 안된다.
    # [2] 동시에 같은 칸에 있을 수 없다.
    # [3] 최소 몇 번 만에 구슬을 뺄 수 있을까
    # [4] 열 번을 넘어가면 실패, -1 출력

    N, M = map(int, input().split())
    board = [list(input()) for _ in range(N)]

    for r in range(N):
        for c in range(M):
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
            nrr, nrc, rmove, r_fell = moving(rr, rc, dr, dc, board)
            nbr, nbc, bmove, b_fell = moving(br, bc, dr, dc, board)

            if b_fell:
                continue

            if r_fell:
                print(depth + 1)
                return
            
            if (nrr, nrc) == (nbr, nbc):
                if rmove > bmove:
                    nrr, nrc = nrr-dr, nrc-dc
                else:
                    nbr, nbc = nbr-dr, nbc-dc

            if visited[nrr][nrc][nbr][nbc] == False:
                q.append((nrr, nrc, nbr, nbc, depth+1))
                visited[nrr][nrc][nbr][nbc] = True

    print(-1)
    pass

bfs()

# 슈퍼베이스 / 버셀
