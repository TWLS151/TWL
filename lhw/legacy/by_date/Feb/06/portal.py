# 포탈

TC = int(input())

for test_case in range(1, TC+1):
    N = int(input())
    portal_lst = list(map(int, input().split()))

    # 매번 오른쪽으로 한 칸씩 이동하고
    # 처음 들어가는 방에서는 그 방의 숫자를 인덱스 취급해 그 방으로 간다.
    # 끝 방에 도달할 때까지 반복
    # 포탈 탄 횟수 종합

    # 한 번 들어간 방은 0 을 할당하고
    # 0인 방에 들어가면 오른쪽으로 한칸 간다

    # 초기 위치
    position = 0  # portal_lst 의 인덱스

    # 카운팅 변수
    count = 0

    # 0인 방에 들어가면 오른쪽으로 이동한다. > portal_lst[position] == 0: postion += 1
    # if portal_lst[position] == 0:
    #     position += 1

    # 방에 숫자가 있으면 그 숫자 인덱스 방으로 이동한다.
    # 포지션이 변한다
    # if portal_lst[position] != 0:
    #     position = portal_lst[position] - 1

    # position 이 N이 될때까지 반복
    while position != N-1:
        if portal_lst[position] == 0:
            position += 1
            count += 1
        # move 변수 없이 해보니까
        # potal_list[postion] = 0 과
        # position = potal_lst[position]
        # 이 두 줄을 동시에 수행하는게 힘들어서 변수를 하나 할당했습니다.
        else:
            move = portal_lst[position]
            portal_lst[position] = 0
            position = move - 1
            count += 1
    print(f'#{test_case} {count}')
