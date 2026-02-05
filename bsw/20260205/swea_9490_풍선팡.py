T = int(input())
for tc in range(1, T + 1):
    N , M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range (N)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    max_val = 0
    for r in range(N):
        for c in range(M):
            pollen_sum = arr[r][c]
            for i in range(4):
                for j in range(1, arr[r][c])
                nr = r + j * dr[i]
                nc = c + j * dc[i]
                if 0 <= nc < M and 0 <= nr < N:
                    pollen_sum += arr[nr][nc]
            
            
            if max_val < pollen_sum:
                max_val = pollen_sum
    print(f'#{tc} {max_val}')


