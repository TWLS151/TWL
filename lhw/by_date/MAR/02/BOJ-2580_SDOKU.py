# BOJ - 2580
# 스도쿠

import sys

N = 9
board = []
zeros = []

row_used = [[False] * 10 for _ in range(9)]
col_used = [[False] * 10 for _ in range(9)]
box_used = [[False] * 10 for _ in range(9)]

def check_box(r, c):  # 박스 체크 함수
    return (r//3)*3 + (c//3)

for r in range(9):
    row = list(map(int, input().split()))
    board.append(row)
    for c in range(9):
        v = row[c]
        if v == 0:
            zeros.append((r, c))
        else:
            row_used[r][v] = True
            col_used[c][v] = True
            box_used[check_box(r, c)][v] = True


def get_candidates(r, c):
    b = check_box(r, c)
    res = []
    for num in range(1, 10):
        if not row_used[r][num] and not col_used[c][num] and not box_used[b][num]:
            res.append(num)
    return res


def dfs():

    if not zeros:
        for r in range(9):
            print(*board[r])
        sys.exit(0)

    best_i = -1
    best_cands = None

    for i, (r, c) in enumerate(zeros):

        cands = get_candidates(r, c)

        if not cands:
            return
        
        if best_cands is None or len(cands) < len(best_cands):
            best_cands = cands
            best_i = i
            if len(best_cands) == 1:
                break

    r, c = zeros.pop(best_i)
    b = check_box(r, c)

    for num in best_cands:
        board[r][c] = num
        row_used[r][num] = True
        col_used[c][num] = True
        box_used[b][num] = True

        dfs()

        row_used[r][num] = False
        col_used[c][num] = False
        box_used[b][num] = False

    zeros.insert(best_i, (r, c))

dfs()