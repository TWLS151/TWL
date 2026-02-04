dc = [-1, 1, 0]
dr = [0, 0, -1] 
# 좌, 우를 우선적으로 탐색하고, 그 다음 위로 올라가는 방식
for tc in range(1, 11):
    T = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    r , c = 99 , 0
    # 역순으로 올라가는 것이기 때문에 처음 위치를 맨 마지막 줄로 정함.
    for i in range(100):
        if ladder[99][i] == 2:
            c = i
            break
    # 도착점인 2를 찾는 과정
    while r > 0:
    # 맨 윗줄로 갈 때까지 반복
        ladder[r][c] = 0
    # 도착점을 0으로 갱신하여 혼동이 생기지 않게 함.
        for num in range(3):
            nc = c + dc[num]
            nr = r + dr[num]
        # 좌, 우, 상 순으로 한칸씩 움직여보는 과정
            if 0<= nr < 100 and 0<= nc< 100 and ladder[nr][nc] == 1:
                r, c = nr, nc
                break
        # 만약에 nr좌표와 nc좌표가 안에 있고, 움직인 좌표가 1일 경우, 위치 갱신 후 브레이크        
    print(f'#{T} {c}')