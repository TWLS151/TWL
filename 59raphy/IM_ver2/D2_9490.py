import sys

sys.stdin = open('input_9490.txt')

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    balloons = [list(map(int, input().split())) for _ in range(N)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    max_pollen = 0

    for r in range(N):
        for c in range(M):
            pollen_cnt = dist = balloons[r][c]

            for d in range(4):
                for i in range(1, dist + 1):
                    nr = r + dr[d] * i
                    nc = c + dc[d] * i
                    if 0 <= nr < N and 0 <= nc < M:
                        pollen_cnt += balloons[nr][nc]
                    else:
                        break

            if max_pollen < pollen_cnt:
                max_pollen = pollen_cnt

    print(f'#{test_case} {max_pollen}')
