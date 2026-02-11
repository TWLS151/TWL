# import sys

# sys.stdin = open('경비병.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1] # 상, 하, 좌, 우
    for r in range(N):
        for c in range(N): 
            if arr[r][c] == 2: # 2인 경우에만
                for i in range(4):
                    for j in range(1, N + 1):
                        nr = r + j * dr[i]
                        nc = c + j * dc[i] # 이동하기
                        if 0 <= nr < N and 0 <= nc < N :
                        # 벽을 안 만났을때의 조건
                            if arr[nr][nc] == 1:
                                break
                            # 기둥을 보면 바로 멈춤
                            else:
                                arr[nr][nc] = 1
                            # 어차피 이 조건에서는 0밖에 없으므로 변경
    cnt = 0
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 0: # 0인 것만 카운트
                cnt+=1
    print(f'#{tc} {cnt}')