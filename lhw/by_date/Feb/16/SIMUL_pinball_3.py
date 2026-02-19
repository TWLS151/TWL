# SWEA - 5650
# 핀볼 게임
# 3트

import sys
sys.stdin = open('input.txt')

dirs = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]
change = {
    1: [1, 3, 0, 2],
    2: [3, 0, 1, 2],
    3: [2, 0, 3, 1],
    4: [1, 2, 3, 0],
    5: [1, 0, 3, 2]
}

def game(r, c, d):
    global wormhole_info
    sr, sc = r, c
    score = 0
    while True:

        dr, dc = dirs[d]
        r += dr
        c += dc

        if board[r][c] == -1 or (r, c) == (sr, sc):
            return score

        if 1 <= board[r][c] <= 5:
            d = change[board[r][c]][d]
            score += 1

        if 6 <= board[r][c] <= 10:
            r, c = wormhole_check[board[r][c]]


TC = int(input())
for test_case in range(1, TC+1):
    N = int(input())
    board = [[5] * (N+2)]
    

    wormhole_info = dict()
    wormhole_check = [0] * 11

    for i in range(1,N+1):
        board.append([5] + list(map(int, input().split())) + [5])
        for j in range(1,N+1):
            if 6 <= board[i][j] <= 10:
                num = board[i][j]
                if not wormhole_check[num]:
                    wormhole_check[num] = (i, j)
                else:
                    wormhole_info[wormhole_check[num]] = (i, j)
                    wormhole_info[(i, j)] = wormhole_check[num]

    board.append([5] *(N+2))

    maxscore = 0
    for sr in range(N):
        for sc in range(N):
            if board[sr][sc] == 0:
                for d in range(4):
                    maxscore = max(maxscore, game(sr, sc, d))

    print(f'#{test_case} {maxscore}')