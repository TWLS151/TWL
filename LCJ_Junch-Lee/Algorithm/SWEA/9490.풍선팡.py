import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):

    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    # 꽃가루 총합 초기값 지정
    max_sum = 0

    # 1. for-1,2 : 각 기준점 별로 꽃가루를 탐색
    for i in range(N):
        for j in range(M):


            # 1-1. 풍선을 터트릴 기준점을 point로 지정
            point = arr[i][j]

            # 2. 기준점 별로 탐색해야할 상하좌우 델타값 리스트 생성
            # 순서 : 상, 하, 좌, 우

            dr = [-1, 1, 0, 0]
            dc = [0, 0, -1, 1]

            # 3. 상하좌우 네 방향에 대해
            for idx in range(4):

                # 4. 풍선이 터지는 범위를 power에 지정
                for power in range(1, arr[i][j] + 1):

                    ni = i + dr[idx]*power
                    nj = j + dc[idx]*power

            ## 2-1. 우하좌상 순서 탐색을 위한 for문 지정
            # for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            #
            #     3-1. 풍선이 터지는 범위는 기준점의 숫자만큼
            #     for power in range(1, arr[i][j] +1):
            #
            #         ni = i + di*power
            #         nj = j + dj*power

                    if 0 <= ni < N and 0 <= nj < M:
                        point += arr[ni][nj]


            if max_sum < point:
                max_sum = point

    print(f"#{tc} {max_sum}")





