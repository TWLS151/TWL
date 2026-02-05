TC = 10

for test_case in range(1, TC+1):
    test_case_num = int(input())

    arr = [list(map(int, input().split())) for _ in range(100)]

    # 각 행, 각 열, 각 대각선의 합 중 최댓값을 구하는 프로그램
    # 대각선은 가장 큰 대각선만 두개
    # 우선 순회하면서 행과 열 합만 구하자.
    # 대각선은 따로 청크를 짜야할 듯

    # 글로벌 최댓값 변수 생성
    maximmum = -(10**99)
    # 행
    for row in arr:
        max_sum_row = sum(row)
        if maximmum < max_sum_row:
            maximmum = max_sum_row
    
    # 열
    for idx in range(100):
        col_lst = []
        for row in arr:
            col_lst.append(row[idx])
        max_sum_col = sum(col_lst)
        if maximmum < max_sum_col:
            maximmum = max_sum_col

    # 대각선 (0, 0) to (99, 99)
    right_down = 0
    for num in range(100):
        right_down += arr[num][num]
    if maximmum < right_down:
        maximmum = right_down

    # 대각선 (0, 99) to (99, 0)
    left_down = 0
    col = 100
    for row in arr:
        col -= 1
        left_down += row[col]
    if maximmum < left_down:
        maximmum = left_down

    print(f'#{test_case} {maximmum}')