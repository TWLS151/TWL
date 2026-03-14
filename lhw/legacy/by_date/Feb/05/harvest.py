# SWEA - 2805



# 농장 크기는 항상 홀수이다.
# 수확은 농장 크기에 딱 들어맞는 마름모만 가능하다.

# 항상 홀수니까 2로 나눈 몫이 가운데값 (인덱스가 0부터니까)
# (0, mid) (mid, 0) (H, mid) (W, mid) 네 점이 기준
# 중앙에서 시작해야하나?
# 중앙에서 시작하고 십자모양은 다 수확 한 다음
# col 값에 변동이 생기면 그만큼 더하고 뺀다
# (mid, mid) 가 중앙
# (mid, mid-1) 이 되면 한 칸 왼쪽으로 이동한거니까
# row 정보는 바꾸기 귀찮으니까 row 를 움직이는걸로 하자
# (mid-1, mid) 가 되면
# 범위는 range(0+1, W-1)
# (mid+1, mid) 가 되면
# range(0+1, W-1) 똑같네?
# for i in range(0, mid):
#     total += arr[row-i][col]
#     for j in range(0 + i, W - i):
#         total += arr[row-i][col+j]

# # (-mid, mid+1) 가 되겠네
# for row_change in range(-mid, mid+1):
#     total += arr[mid+row_change][mid]
#     for col_change in range(0+i, N-i):
#         total += arr[mid+row_change][mid+col_change]

tc = int(input())

for test_case in range(1, tc+1):
    N = int(input())  # 7
    farm_size = [list(map(int, input())) for _ in range(N)]
    # farm_size = [input() for _ in range(N)]  # 7 * 7

    mid = N // 2  # 3
    total = 0 

    # 중앙에서부터 위 아래로 움직임
    for row_change in range(-mid, mid + 1):
        for col in range(abs(row_change), N - abs(row_change)):
            total += farm_size[mid + row_change][col]
    print(f'#{test_case} {total}')


# 로직은 맞았는데 열의 범위를 잘못 설정해서 질질 끌었다 30분 안에 풀 수 있을 정도의 문제
# 표현하는 과정에서 사고가 조금 꼬였다. 다음 번엔 이런 일 없도록 해보자
# 