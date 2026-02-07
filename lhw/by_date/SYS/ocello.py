# SWEA - 4615

tc = int(input())

for test_case in range(1, tc + 1):
    pass

    M, times = map(int, input().split())

    field = [[0] * (M) for _ in range(M)]

    # 필드 세팅부터 하자 가운데 흑돌 백돌 놓기
    # field_size / 2 - 1 백
    # field_size / 2 백
    # (field_size/2, field_size/2) (field_size/2 - 1, field_size/2 - 1) 백
    # (field_size/2, field_size/2 - 1) (field_size/2 - 1, field_size/2) 흑
    

    field[M//2][M//2], field[M//2-1][M//2-1] = 2, 2
    field[M//2][M//2-1], field[M//2-1][M//2] = 1, 1

    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for order in range(times):
        row, col, colour = map(int, input().split())

        row -= 1
        col -= 1

        # 돌 놓기
        field[row][col] = colour
        # for 문으로 돌 놓은 자리부터 상하좌우 보기
        # 0 만나면 브레이크
        # 다른 색 만나면 쭉
        # 같은 색 만나면 사이에 값 다 같은걸로 바꾸고 브레이크
        # for tempt in range(1, M):
        #     for drow, dcol in dirs:
        #         nrow, ncol = row + drow * tempt, col + dcol * tempt
        #         if 0 <= nrow < M and 0 <= ncol < M:
        #             if field[nrow][ncol] == 0:

        #         else:
        #             break    
        # while 문으로 설계해볼까?
        idx = 0
        while idx < 4:
            drow, dcol = dirs[idx]
            nrow, ncol = row + drow, col + dcol
            if 0 <= nrow < M and 0 <= ncol < M:
                if field[nrow][ncol] == 0:
                    break
                if field[nrow][ncol] != field[row][col]:
                    change_lst = [field[nrow][ncol]]
                    while 0 <= nrow < M and 0 <= ncol < M:
                        nrow += drow
                        ncol += dcol

                        if field[nrow][ncol] == 0:
                            break
                        if field[nrow][ncol] == field[row][col]:
                            for i in change_lst:
                                i = colour
                            idx += 1
                            break
                        change_lst.append(field[nrow][ncol])
                if field[nrow][ncol] == field[row][col]:
                    break
            idx += 1
                



    count = 0
    for row in range(M):
        for col in range(M):
            if field[row][col] == 1:
                count += 1
    
    print(f'#{test_case} {M*M - count} {count}')
