import sys

sys.stdin = open('input_1210.txt')

T = 10

for test_case in range(1, T + 1):
    tc = input()
    ladder = [list(map(int, input().split())) for _ in range(100)]

    # 가장 마지막 줄(99행)에서 도착 지점 '2'가 있는 열의 인덱스를 찾음
    c = ladder[99].index(2)

    # 바닥 바로 위(98번 행)부터 2번째 위(1행)까지 역순으로 탐색
    for r in range(98, 0, -1):
        # 1) 왼쪽(c-1)에 가로 막대(1)가 있는지 확인
        if c > 0 and ladder[r][c-1] == 1:
            # 길이 없을 때까지 왼쪽으로 이동
            while c > 0 and ladder[r][c-1] == 1:
                c -= 1
        # 2) 오른쪽(c+1)에 가로 막대(1)가 있는지 확인
        elif c < 99 and ladder[r][c+1] == 1:
            # 길이 없을 때까지 오른쪽으로 이동
            while c < 99 and ladder[r][c+1] == 1:
                c += 1
        # 3) 가로 막대가 없으면 다음 행으로 올라감

    # 모든 행을 다 올라와 루프가 끝났을 때의 열 인덱스(c)가 곧 출발점
    print(f'#{tc} {c}')
