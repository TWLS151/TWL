import sys

sys.stdin = open('input_p13_1949.txt')

"""
[문제]
N * N 크기의 지도가 주어지고, 각 칸에는 지형의 높이가 적혀 있다.
하산 규칙은 다음과 같다.

1. 가장 높은 봉우리 중 하나를 선택하여 시작한다.
2. 반드시 높은 지형에서 낮은 지형으로, 가로 또는 세로 방향으로 이동해야 한다.
   즉, 높이가 같은 곳 혹은 낮은 지형이나, 대각선 방향의 연결은 불가능하다.
3. 이동 가능한 방향이 여러 곳이라도, 항상 높이 차이가 가장 큰 곳으로만 이동한다.
   차이가 같은 곳이 여러 개라면 상-하-좌-우 우선순위를 따른다.
4. 시작점에서 출발하여 더 이상 내려갈 곳이 없을 때까지 이동했을 때, 지나온 경로의 길이(칸 수)를 구한다.

가장 긴 하산 경로를 찾아 그 길이를 출력하는 프로그램을 작성하라.

[제약 사항]
1. 지도의 한 변의 길이 N은 3 이상 8 이하의 정수이다. (3 ≤ N ≤ 8)
2. 지도에 나타나는 지형의 높이는 1 이상 20 이하의 정수이다.
3. 지도에서 가장 높은 봉우리는 최대 5개이다.
4. 지형을 깎는 공사 기능은 없다.
"""

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    peaks = [list(map(int, input().split())) for _ in range(N)]

    highest_peak = []
    """
    # max 사용 시
    h = max(max(row) for row in peaks)
    """
    h = 20

    while not highest_peak:
        for i in range(N):
            for j in range(N):
                if peaks[i][j] == h:
                    highest_peak.append([i, j])
        h -= 1

    # 방향 벡터 : 제자리(0), 상(1), 하(2), 좌(3), 우(4)
    # -x 정렬을 위해 '제자리'를 인덱스 0에 두어 우선순위를 가장 높게 설정함
    dr = [0, -1, 1, 0, 0]
    dc = [0, 0, 0, -1, 1]

    max_route = 1

    for r, c in highest_peak:
        route_cnt = 1
        nr, nc = r, c

        while True:
            # 경계 검사를 통과한 유효한 방향 인덱스 리스트 생성
            possible_d = [i for i in range(5) if 0 <= nr+dr[i] < N and 0 <= nc+dc[i] < N]

            # 정렬 기준 : 1) 높이 차이 최대, 2. 인덱스 번호 최소(-x)
            # 만약 상하좌우가 모두 높으면 1~4 인덱스의 차이값이 음수가 됨
            # 차이가 0인 '제자리'가 최댓값으로 선택됨
            d = max(possible_d, key=lambda x: (peaks[nr][nc] - peaks[nr+dr[x]][nc+dc[x]], -x))
            # 선택된 방향이 '제자리'라면 이동 불가 상태로 루프 종료(break)
            if d == 0:
                break
            # 차이가 가장 큰 방향으로 이동 및 경로 카운트
            else:
                nr += dr[d]
                nc += dc[d]
                route_cnt += 1

        # 최댓값 갱신
        if max_route < route_cnt:
            max_route = route_cnt

    print(f'#{test_case} {max_route}')
