for _ in range(10):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    
    # 도착점(2) 찾기
    cr = 99
    cc = ladder[99].index(2)
    
    # 델타: 좌, 우, 상
    dr = [0, 0, -1]
    dc = [-1, 1, 0]
    
    # 맨 윗줄(cr == 0)에 도달할 때까지 반복
    while cr > 0:
        # 1. 현재 위치를 0으로 지워서 다시 돌아가지 않게 만듦
        ladder[cr][cc] = 0 
        
        # 2. 좌 -> 우 -> 상 순서로 탐색
        for i in range(3):
            nr = cr + dr[i]
            nc = cc + dc[i]
            
            # 3. 맵 범위를 벗어나지 않고, 이동할 곳이 길(1)이라면
            if 0 <= nr < 100 and 0 <= nc < 100 and ladder[nr][nc] == 1:
                cr, cc = nr, nc
                break 
                

    print(f"#{tc} {cc}")