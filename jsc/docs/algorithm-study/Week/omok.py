import sys

dr = [-1, 1, 0, 0, -1, -1, 1, 1]
dc = [0, 0, -1, 1, -1, 1, -1, 1]

def flip(r, c, d, color, path):
    nr, nc = r + dr[d], c + dc[d]

    if not (0 <= nr < N and 0 <= nc < N) or board[nr][nc] == 0:
        return False
    
    if board[nr][nc] == color:
        if path:
            return True
        else:
            return False
        
    if board[nr][nc] != color:
        path.append((nr, nc))
        if flip(nr, nc, d, color, path):
            return True
        else:
            return False


    pass


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input())
    board = [[0] * N for _ in range(N)]    

    mid = N // 2
    board[mid - 1][mid - 1] = 2
    board[mid][mid - 1] = 1
    board[mid - 1][mid] = 1
    board[mid][mid] = 2

    for _ in range(M):
        c, r, color = map(int, input().split())
        r, c = r-1, c-1

        if board[r][c] != 0: continue
        board[r][c] = color

        for d in range(8):
            path = []
            if flip(r, c, d, color, path):
                for pr, pc in path:
                    board[pr][pc] = color

    

        

        