# SWEA - 4615

tc = int(input())

for test_case in range(1, tc + 1):
    pass

    field_size, times = map(int, input().split())

    field = [[0] * (field_size) for _ in range(field_size)]

    # 필드 세팅부터 하자 가운데 흑돌 백돌 놓기
    # field_size / 2 - 1 백
    # field_size / 2 백
    # (field_size/2, field_size/2) (field_size/2 - 1, field_size/2 - 1) 백
    # (field_size/2, field_size/2 - 1) (field_size/2 - 1, field_size/2) 흑

    field[int(field_size/2)][int(field_size/2)], field[int(field_size/2)-1][int(field_size/2)-1] = 2, 2
    field[int(field_size/2)][int(field_size/2)-1], field[int(field_size/2)-1][int(field_size/2)] = 1, 1

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
        for drow, dcol in dirs:
            nr, nc = row + drow, col + dcol
            if 0 <= nr < field_size and 0 <= nc < field_size:
                while 0 <= nr < field_size and 0 <= nc < field_size and field[nr][nc] != field[row][col]:
                    if field[nr][nc] == 0:
                        break
                    if field[nr][nc] != field[row][col]:
                        if field[nr][nc] == 1:
                            field[nr][nc] = 0
                        else:
                            field[nr][nc] = 1    
                        nr += drow
                        nc += dcol
                    else:
                        break

    count = 0
    for row in range(field_size):
        for col in range(field_size):
            if field[row][col] == 1:
                count += 1
    
    print(f'#{test_case} {field_size*field_size - count} {count}')
