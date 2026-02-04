T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    # 우, 하, 좌, 상 순으로 좌표를 매김.
    r , c = 0, 0
    direction = 0
    count = 1
    # 출발하는 좌표가 [0,0]이므로 초기 위치를 [0,0]으로 잡음. 
    # 움직이는 방향이 오른쪽이므로 direction을 0으로 잡음.
    # 좌표를 기록한 초기 좌표를 1로 지정
    for _ in range(0, N ** 2):
        arr[r][c] = count
        count += 1
        # 현재 존재하는 위치에 좌표를 찍고 1을 더함.
        nr = r + dr[direction]
        nc = c + dc[direction]
        # 현재 위치에서 변하는 위치를 기록
        if not (0<= nr < N and 0 <= nc < N) or arr[nr][nc] !=0:
            direction = (direction + 1) % 4
            nr = r + dr[direction]
            nc = c + dc[direction]
        # if 문의 문장은 벽을 만났거나, 리스트의 값이 0이 아닌 수를 만났을때의 조건,
        # 방향을 1만큼 증가시켜 회전시키고, 그 자리에는 이미 수가 찍혀 있으므로 바라보고 있는 방향으로 이동
        r = nr
        c = nc
        # 위치 갱신
    print(f'#{tc}')
    for row in arr:
        print(f'{" ".join(map(str, row))}')
    # arr에 존재하는 숫자를 문자로 변환시키고 join을 이용하여 출력

