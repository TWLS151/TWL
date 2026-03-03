import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):

    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    # 1. 배열 전체를 순회
    # 1-1. 최대값 변수 초기화
    max_total = 0

    # 주의 ! 파리채가 격자를 벗어나는 경우는 계산할 필요가 없음
    # 계산량을 줄이는 방법
    # range(N) -> range(N-M+1)
    # 행, 열의 마지막 인덱스에서는 파리채를 내려칠 수 없음 !!

    for r in range(N-M+1):
        for c in range(N-M+1):

            # 2. 기준점 별 파리의 합계 total을 초기화
            total = 0

            # 3. 기준점 total 을 중심으로 (M x M) 범위를 탐색
            # M x M 범위를 탐색하고자 할 경우, + 1 ~ (M-1) 범위를 탐색해야함
            for dr in range(0, M):
                for dc in range(0, M):

                    ni = r + dr
                    nj = c + dc

                    total += arr[ni][nj]

                    # 3-1. 배열 범위 안인 경우, 해당 칸의 파리 수를 합계에 더함
                    # if ni < N and nj < N:
                    #
                    #     total += arr[ni][nj]
                    # ==> 필요 없는 조건탐색.

            # 4. M x M 범위를 탐색한 후, 최대값과의 비교

            if max_total < total:
                max_total = total

    print(f"#{tc} {max_total}")
