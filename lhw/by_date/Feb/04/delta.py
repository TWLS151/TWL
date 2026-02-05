TC = int(input())

for test_case in range(1, TC + 1):
    N = int(input())
    # 행렬 생성
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 위, 아래, 오른쪽, 왼쪽 순서 리스트 생성
    dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    # 총 합계 변수
    total = 0
    
    # 행렬 순회
    for row in range(N):
        for col in range(N):

            # 방향 리스트 순회
            for idx in dir:
                # 차의 총합을 기록할 변수 생성
                total_diff = 0
                # 방향 설정 후 그 방향에 필드가 있을 때만 연산
                if 0 <= row + idx[0] < N and 0 <= col + idx[1] < N:
                    next_row, next_col = row + idx[0], col + idx[1]
                    diff = arr[row][col] - arr[next_row][next_col]
                    # 만약 차가 음수값이 나오면
                    if diff < 0:
                        # 양수로 반환
                        diff = -diff
                    # 차의 총합 기록
                    total_diff += diff
                # 차의 총합 합계
                total += total_diff
    # 출력
    print(f'#{test_case} {total}')