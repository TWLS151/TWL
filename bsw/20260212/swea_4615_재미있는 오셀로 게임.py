import sys

sys.stdin = open('swea_4615_재미있는 오셀로 게임.txt')

T = int(input())
for test_case in range(1, T + 1):
    N , M = map(int, input().split())
    info_lst = [list(map(int, input().split())) for _ in range(M)]
    arr = [[0] * N for _ in range(N)]
    dr = [-1, 1, 0, 0, -1, 1, -1, 1]
    dc = [0, 0, -1, 1, 1, -1, -1, 1] # 8방향 지정
    arr[N//2][N//2] = 2
    arr[N//2-1][N//2] = 1
    arr[N//2][N//2-1] = 1
    arr[N//2-1][N//2-1] = 2 # 미리 가운데에 돌 두기
    for r_, c_, color in info_lst:
        r , c = r_ - 1, c_ - 1 # 인덱스 조정
        arr[r][c] = color # 일단 내 위치에 돌을 둬
        for i in range(8):
            nr, nc = r + dr[i], c + dc[i]
            duigip_lst = []
            while 0<= nr< N and 0<= nc< N: # 벽에 박으면 종료
                if arr[nr][nc] == 0: # 아무것도 없으면 바로 끝
                    break
                if arr[nr][nc] == color: # 같은 색이면
                    for tr, tc in duigip_lst: # 뒤집을 리스트를 모두 같은 색으로
                        arr[tr][tc] = color
                    break
                else:
                    duigip_lst.append((nr , nc)) # 다른 색이면 뒤집을 리스트에 추가
                    nr += dr[i] # 같은 방향으로 계속 전진!
                    nc += dc[i] 

    white_lst, black_lst = 0, 0
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 1:
                black_lst += 1
            elif arr[r][c] == 2:
                white_lst += 1
    # black_lst = sum(row.count(1) for row in arr)
	  # white_lst = sum(row.count(2) for row in arr)
	  # 위의 개수 세는 것을 리팩토링 받으니 이렇게 쉽게 구할 수도 있다 하네요.
    print(f'#{test_case} {black_lst} {white_lst}')


