T = int(input())
for tc in range(1, T + 1):
    total_arr = [[0] * 10 for _ in range(10)]
    # [0]이 10 * 10 구간으로 채워진 영역 생성
    arr_num = int(input())
    for arr in range (arr_num):
        r1, c1, r2, c2, color_type = map(int, input().split())
        # 각각의 행과 열, 그리고 색깔 타입을 정의함.
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                total_arr[i][j] += color_type
        # input된 범위에 해당하는 구간을 red or blue에 따라 다른 값을 추가함.
        count = 0
        for i in total_arr:
            for j in i:
                if j == 3:
                    count += 1 
        # 카운트를 각 범위마다 초기화를 시킴.
        # 색이 겹치는 보라색은 color_type이 3이므로 보라색을 만나면 출력값을 1씩 추가
    print(f'#{tc} {count}')

        