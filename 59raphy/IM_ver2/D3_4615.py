import sys

sys.stdin = open('input_4615.txt')

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input(). split())
    play = [list(map(int, input().split())) for _ in range(M)]
    board = [[0] * N for _ in range(N)]

    # 초기 배치
    n = N // 2
    board[n][n-1], board[n-1][n] = 1, 1  # 중앙 좌하단, 우상단 흑돌
    board[n][n], board[n-1][n-1] = 2, 2  # 중앙 우하단, 좌상단 백돌

    # 방향 벡터
    dr = [-1, 1, 0, 0, -1, -1, 1, 1]
    dc = [0, 0, -1, 1, -1, 1, -1, 1]

    for x, y, player in play:
        # 입력 좌표(열행, 1-base)를 배열의 인덱스(행열, 0-base)로 변환
        r = y - 1
        c = x - 1

        """
        if player == 1:   # 현재 플레이어가 흑돌(1)인 경우
            opponent = 2  # 상대방은 백돌(2)로 설정
        else:             # 현재 플레이어가 백돌(2)인 경우
            opponent = 1  # 상대방은 흑돌(1)로 설정
        """
        opponent = 3 - player

        # 해당 좌표에 돌 놓음
        board[r][c] = player

        # 8방향 탐색
        for d in range(8):
            change = []  # 뒤집을 상대 돌의 좌표를 담을 리스트
            nr = r + dr[d]  # 이동 좌표
            nc = c + dc[d]

            while 0 <= nr < N and 0 <= nc < N:
                # 빈 칸이면 해당 방향 탐색 중단
                if board[nr][nc] == 0:
                    break

                # 내 돌이면 리스트에 쌓인 상대 돌을 뒤집고 탐색 중단
                # 인접한 돌이 내 돌이면 빈 리스트이므로 변화 없음
                elif board[nr][nc] == player:
                    for i, j in change:
                        board[i][j] = player
                    break

                # 상대 돌이면 리스트에 좌표를 추가하고 한 칸 전진
                else:
                    change.append([nr, nc])
                    nr += dr[d]
                    nc += dc[d]

    # 최종 보드판에서 흑돌과 백돌 개수 카운트
    b_cnt, w_cnt = 0, 0
    for r in range(N):
        for c in range(N):
            if board[r][c] == 1:
                b_cnt += 1
            # [PITFALL] 종료 후에도 빈 칸이 있을 수 있으므로 'else:'를 카운트하지 않도록 주의
            elif board[r][c] == 2:
                w_cnt += 1

    print(f'#{test_case} {b_cnt} {w_cnt}')
