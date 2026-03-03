for tc in range(1, 11):
    N = int(input())
    total_range = [list(map(int, input().split())) for _ in range(100)]
    # 영역에 input 값을 구현
    sum_lst = []
    row_sum = 0
    column_sum = 0
    diagonal_sum = 0
    diagonal_sum2 = 0
    # 행, 열, 2개의 대각선의 합을 담을 빈 리스트와 변수들을 지정
    for r in range(100):
        for c in range(100):
            row_sum += total_range[r][c]
            column_sum += total_range[c][r]
        sum_lst.append(row_sum)
        sum_lst.append(column_sum)
        # 행, 열의 합을 한줄씩 구하고 sum_lst에 추가
        row_sum = 0
        column_sum = 0
        # 이후 0으로 초기화
    for rc in range(100):
        diagonal_sum += total_range[rc][rc]
        diagonal_sum2 += total_range[rc][99-rc]
        # 대각선은 1번만 구하면 되기 때문에 합 구하고 초기화 x
        # 대각선의 합을 구하기 위하여 범위를 다르게 설정
    sum_lst.append(diagonal_sum)
    sum_lst.append(diagonal_sum2)
    print(f'#{N} {max(sum_lst)}')
    # 최댓값을 출력
    

#######################################################################

# 아래는 AI한테 리팩토링 받은 코드

def calc_sum(r, c, dr, dc):
    line_sum = 0
    # 100x100이 고정이므로 100번 반복하거나, 범위 체크를 하며 반복
    for _ in range(100):
        line_sum += arr[r][c]
        r += dr
        c += dc
    return line_sum
for _ in range(1, 11):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    max_sum = 0
    # 1. 가로(행) 검사: 시작점 (i, 0), 방향 (0, 1)
    for i in range(100):
        max_sum = max(max_sum, calc_sum(i, 0, 0, 1))    
    # 2. 세로(열) 검사: 시작점 (0, i), 방향 (1, 0)
    for i in range(100):
        max_sum = max(max_sum, calc_sum(0, i, 1, 0))   
    # 3. 우하향 대각선 (Main Diagonal): 시작점 (0, 0), 방향 (1, 1)
    max_sum = max(max_sum, calc_sum(0, 0, 1, 1))   
    # 4. 좌하향 대각선 (Anti Diagonal): 시작점 (0, 99), 방향 (1, -1)
    max_sum = max(max_sum, calc_sum(0, 99, 1, -1))
    print(f'#{tc} {max_sum}')
