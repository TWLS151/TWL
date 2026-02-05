T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_sum = 0
    for r in range(N):
        for c in range(N):
            sum = 0 # 합을 0으로 만들어놓기
            for i in range(M):  
                for j in range(M):  
                    nc = c + j  # 영역을 훑는 과정
                    
                    if 0 <= nc < N and 0 <= i + r< N:
                        sum += arr[i + r][nc]
                    # 벽에 안 박을때만 이동한 좌표의 값을 더함.
            if max_sum < sum:
                max_sum = sum
            # 더 큰값이 있으면 대체
    
    print(f'#{tc} {max_sum}')