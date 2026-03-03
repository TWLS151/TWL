import sys

sys.stdin = open('등산로 조성.txt')

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    map_info = [list(map(int, input().split())) for _ in range(N)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    max_val = map_info[0][0]
    for r in range(N):
        for c in range(N):
            if max_val < map_info[r][c]:
                max_val = map_info[r][c]
    for r in range(N):
        for c in range(N):
            count = 0
            if map_info[r][c] == max_val:
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if (0<= nr < N and 0 <= nc < N) and map_info[nr][nc] < map_info[r][c]:
                        r , c = nr, nc
                        count += 1
                        break
                    else:
                        pass
    print(f'#{tc} {count}')