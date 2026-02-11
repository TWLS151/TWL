import sys
# sys.stdin = open('./TWL/LCJ_Junch-Lee/Algorithm/IM_exam/input.txt','r')
sys.stdin = open('input.txt', 'r')
T = int(input())

def find_guard(arr, N):

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for r in range(N):
        for c in range(N):

            if arr[r][c] == 2:

                for d in range(4): # 방향
                    for s in range(1, N): # 범위(scope)

                        nr = r + dr[d]*s
                        nc = c + dc[d]*s

                        if 0 <= nr < N and 0 <= nc < N: # 주의 1 : 벽을 만나면 해당 방향은 종료
                            if arr[nr][nc] == 1:        # 멈추고 다음 방향으로
                                break
                            else:
                                arr[nr][nc] = 2

                else: return arr # 주의 2 : 경비병 발견 시, 가능 구역 계산 후 바로 함수 종료


for tc in range(1, T+1):

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    safe_arr = find_guard(arr, N)
    count = 0

    for row in safe_arr:
        for idx in range(N):
            
            if row[idx] == 0:

                count +=1

    print(f"#{tc} {count}")