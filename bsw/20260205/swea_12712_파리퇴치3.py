T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_sum = 0
    dr = [-1, 1, 0, 0, -1, 1, 1, -1]
    dc = [0, 0, -1, 1, -1, 1, -1, 1]
    # 8개의 방향 미리 작성
    for r in range(N):
        for c in range(N):
            sum1 = arr[r][c] # 가운뎃 값 미리 저장
            for i in range(4):
                for j in range(1, M):    
                    nr, nc = r + j * dr[i], c + j * dc[i] # 4방향으로 이동하는 과정
                    if 0 <= nr < N and 0 <= nc < N:
                        sum1 += arr[nr][nc]
                    # 벽에 안 박을때만 이동한 좌표의 값을 더함.
            sum2 = arr[r][c]   
            for i in range(4, 8):
                for j in range(1, M):    
                    
                    nr, nc = r + j * dr[i], c + j * dc[i]
                    if 0 <= nr < N and 0 <= nc < N:
                        sum2 += arr[nr][nc]
                    
            if max_sum < sum1:
                max_sum = sum1
            if max_sum < sum2:
                max_sum = sum2
            # 최댓값이 있으면 대체
    
    print(f'#{tc} {max_sum}')