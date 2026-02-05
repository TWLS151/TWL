import sys

sys.stdin = open('input.txt', 'r')

T = int(input())


for tc in range(1, T+1):

    arr = [[0]*10 for _ in range(10)]

    # 1. 입력받을 값 : N(색칠 개수)
    N = int(input())

    # 2. 색칠 수 만큼 반복
    for _ in range(N):

        # 3. 색칠의 시작점(_s)과 끝 점(_e)을 각각 정수로 입력
        row_s, col_s, row_e, col_e, color = map(int, input().split())

        # 4. 색칠 범위에 해당하는 영역에 color 별 숫자를 더함
        # red = 1, blue = 2
        for r in range(row_s, row_e + 1):
            for c in range(col_s, col_e + 1):

                arr[r][c] += color

    # 5. 배열 내에 겹친 영역(값이 3이상)을 count
    count = 0

    for r in range(10):
        for c in range(10):

            if arr[r][c] >= 3:
                count += 1

    print(f"#{tc} {count}")