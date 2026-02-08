T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    r = 0
    c = 0
    direction = 0
    count = 1
    for i in range(N ** 2): 
        arr[r][c] = count
        count += 1
        nr = r + dr[direction]
        nc = c + dc[direction]
        if not (0<= nr < N and 0<= nc < N) or arr[nr][nc] != 0:
            direction = (direction + 1) % 4
            nr = r + dr[direction]
            nc = c + dc[direction]
        r = nr
        c = nc
    print(f'#{tc}')
    for row in arr:
        print(*row)