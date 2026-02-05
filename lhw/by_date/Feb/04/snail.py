TC = int(input())

for test_case in range(1, TC+1):
    N = int(input())

    arr = [[0]*N for _ in range(N)]

    # 오른쪽, 아래, 왼쪽, 위 순서
    dir = [
        [0, 1],
        [1, 0],
        [0, -1],
        [-1, 0]
    ]
    # 모든 칸의 값은 현재 0
    # 이동 예정인 칸의 값이 0이면 num으로 교체
    # 0이 아니거나 필드 밖으로 나가면 우회전

    # 현재 위치 값 변수 생성 및 출발지 값 할당
    pos = [0, 0]
    arr[0][0] = 1

    # 각 위치에 할당할 변수 생성
    num = 1

    # 숫자 할당이 끝날때까지 전체 반복
    while num != N**2:
        # 큰 while 문이 끝날때까지 방향리스트 반복 순회
        for direction in dir:
            # 숫자 할당이 끝나면 반복문 탈출
            if num == N**2:
                break
            # 이미 숫자가 할당되어 있는 칸을 만나거나 필드 밖으로 나갈때 까지 반복하는 작은 반복문
            while num != N**2:
                # 전체 크기에 숫자 할당이 끝나면 작은 반복문 탈출
                if num == N**2:
                    break
                # 델타 계산을 위한 포지션의 좌표값과 방향의 좌표값 추출   
                px, py = pos
                dx, dy = direction
                # 필드 밖으로 나가지 않도록 하는 조건문
                if 0 <= px + dx < N and 0 <= py + dy < N:
                    # 숫자가 이미 할당되어 있는 칸을 만나면 작은 반복문 탈출
                    if arr[px + dx][py + dy] != 0:
                        break
                    # 다음 칸으로 진행할 수 있는 상태라고 판단되면 num + 1 후
                    num += 1
                    # 증가한 num 다음 칸에 할당
                    arr[px + dx][py + dy] = num
                    # 그리고 이동
                    pos = [px + dx, py + dy]
                # 필드 밖으로 나가면 방향 변경을 위해 작은 반복문 탈출
                else:
                    break

    # 출력
    print(f'#{test_case}')
    for i in range(N):
        print(f'{" ".join(map(str, arr[i]))}')