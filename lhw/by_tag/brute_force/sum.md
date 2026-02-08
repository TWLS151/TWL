# CAL. SUM.
## BRUTEFORCE, TIME EFFICIENCY

- 문제의 난이도는 매우 낮아 어떻게 풀어도 풀 수 있지만
- 추후 비슷한 문제를 만나면 솔루션처럼 풀고 싶어 기록합니다.

- 항상 행과 열을 계산할때 따로 따로 반목문을 두개를 사용해왔는데
- 솔루션의 두번째 for문 처럼 그냥 row 와 col 의 값을 바꿔주면 두개가 동시에 계산이 됩니다.
- 대각선 계산 또한 그렇습니다.

# 솔루션
```python
# 10개의 테스트 케이스 반복
for _ in range(10):
    tc = int(input())
    grid = [list(map(int, input().split())) for _ in range(100)]

    # 최대 합, 두 대각선의 합을 저장할 변수 초기화
    max_sum = 0
    diag1_sum = 0  # 좌상단 -> 우하단
    diag2_sum = 0  # 우상단 -> 좌하단

    for i in range(100):
        # 각 i번째 순회에서 행과 열의 합을 계산하기 위한 변수
        row_sum = 0
        col_sum = 0

        # 대각선 합 누적
        diag1_sum += grid[i][i]
        diag2_sum += grid[i][99 - i]

        for j in range(100):
            # i번째 행의 합과 j번째 열의 합을 각각 누적
            row_sum += grid[i][j]
            col_sum += grid[j][i]

        # i번째 행/열의 합과 기존 최대값 비교 후 갱신
        if max_sum < row_sum:
            max_sum = row_sum
        if max_sum < col_sum:
            max_sum = col_sum

    # 모든 행/열의 합 계산 후, 최종적으로 대각선 합과 비교
    if max_sum < diag1_sum:
        max_sum = diag1_sum
    if max_sum < diag2_sum:
        max_sum = diag2_sum

    print(f"#{tc} {max_sum}")

```


```python
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
```