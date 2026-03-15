TC = int(input())

for test_case in range(1, TC+1):
    area_num = int(input())
    area_lst = [list(map(int, input().split())) for _ in range(area_num)]
    # input 끝

    # 10 x 10 모눈종이가 있다.
    grid = [[0] * 10 for _ in range(10)]

    # 모눈 종이를 색칠해보자

    # area_lst = [구역 시작 row, 구역 끝 row, 구역 시작 col, 구역 끝 col, 색]
    # 언패킹
    # start_row, end_row, start_col, end_col, colour = area_lst[idx]
    # range 를 잡자
    # row_range = range(start_row, end_row)
    # col_range = range(start_col, end_col)

    # 보라색으로 색칠되면 카운트 할 변수 추가
    violet_count = 0

    # 위에서 정한 변수 지정
    for area in area_lst:
        start_row, start_col, end_row, end_col, colour = area
        # 1은 빨강 2는 블루
        if colour == 1:
            colour = 'R'
        else:
            colour = 'B'

        # 두 범위 안에 있는 칸은 colour 로 색칠
        # 경우의 수 3가지 = [비어있을 때, 빨간색일 때, 파란색일 때] (같은 색은 안겹친다는 조건 명시되어 있음)
        # 그리드 내 지정 범위를 순회하며 0 이면 색칠, 색이 있으면 보라색으로 변환 및 카운팅
        for row in range(start_row, end_row + 1):
            for col in range(start_col, end_col + 1):
                if grid[row][col] == 0:
                    grid[row][col] = colour
                # 0이 아닌 경우는 다른 색이 칠해져 있는 경우밖에 없음
                else:
                    grid[row][col] = 'V'
                    violet_count += 1

    print(f'#{test_case} {violet_count}')