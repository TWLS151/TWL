# SWEA - 5650
# 핀볼 게임
# 2회차

import sys
sys.stdin = open('input.txt')

# 상태 정의, 반복 단위, 이동, 후처리, 갱신

# 1, 2, 3, 4, 5 블럭
# 6~10 웜홀
# -1 블랙홀

directions = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
]
change = {
    1: [1, 3, 0, 2],
    2: [3, 0, 1, 2],
    3: [2, 0, 3, 1],
    4: [1, 2, 3, 0],
    5: [1, 0, 3, 2]
}

def pinball(r, c, d):
    global wormhole_info
    score = 0
    sr, sc = r, c

    while True:
        dr, dc = directions[d]
        r += dr
        c += dc

        if (r, c) == (sr, sc) or board[r][c] == -1:
            return score
        if 1<= board[r][c] <= 5:
            d = change[board[r][c]][d]
            score += 1
        elif 6<= board[r][c] <= 10:
            r, c = wormhole_info[(r, c)]

TC = int(input())
for test_case in range(1, TC+1):
    N = int(input())
    wormhole_check = [0]*11
    wormhole_info = dict()

    board = [[5]*(N+2)]

    for i in range(1, N+1):
        board.append([5] + list(map(int, input().split())) + [5])
        for j in range(1, N+1):
            if 6<= board[i][j] <= 10:
                num = board[i][j]
                if not wormhole_check[num]:
                    wormhole_check[num] = (i, j)
                else:
                    wormhole_info[wormhole_check[num]] = (i, j)
                    wormhole_info[(i, j)] = wormhole_check[num]    
    board.append([5]*(N+2))

        
    score = float('-inf')
    for sr in range(1,N+1):
        for sc in range(1,N+1):
            if board[sr][sc] == 0:
                for sd in range(4):
                    score = max(score, pinball(sr, sc, sd))
    
    print(f'#{test_case} {score}')