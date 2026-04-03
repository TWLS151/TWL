import sys
sys.stdin = open('swea-1954.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    board = [[0] * N for _ in range(N)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    nr = 0
    nc = 0
    visited = [[False] * N for _ in range(N)]
    cnt = 1


    for dir in range(4):
        while True:
            if cnt == N*N:
                break

            if not (0 <= nr + dr[dir] < N and 0 <= nc + dc[dir] < N) or visited[nr + dr[dir]][nc + dc[dir]] != 0:
                break

            if nr == 0 and nc == 0:
                if 0 <= nr + dr[dir] <= N - 1 and 0 <= nr + dr[dir] <= N -1:
                    visited[nr][nc] = cnt
                    cnt += 1
                    nr += dr[dir]
                    nc += dc[dir]
                

            elif 0 <= nr <= N-1 and 0 <= nc <= N-1 and visited[nr][nc] == True:
                if 0 <= nr + dr[dir] <= N - 1 and 0 <= nr + dr[dir] <= N -1:
                    visited[nr][nc] = cnt
                    cnt += 1
                    nr += dr[dir]
                    nc += dc[dir]
    else:
        print(visited)