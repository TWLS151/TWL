# 무선 충전
# 0212 // 0242

import sys
sys.stdin = open('a.txt')

directions = [
    (0, 0), (-1, 0), (0, 1), (1, 0), (0, -1)
]



TC = int(input())

for test_case in range(1, TC+1):
    pass
    M, A = map(int, input().split())  # 경과 시간, 충전소 수
    a_dir = list(map(int, input().split()))
    b_dir = list(map(int, input().split()))

    AP_info = {}
    AP_idx = [0]
    for _ in range(A):
        y, x, C, P = map(int, input().split())
        AP_info[(x, y)] = [C, P]
        AP_idx.append((x, y))

    field = [[0 for _ in range(11)] for _ in range(11)]
    pos_field = [[0 for _ in range(11)] for _ in range(11)]
    # 충전소 범위 표시해야겠는데
    # 좌표에 성능값을 맥여버리자
    for idx in range(1, A+ 1):
        vx, vy = AP_idx[idx]
        cover, power = AP_info[AP_idx[idx]]
        
        for i in range(-cover, cover + 1):
            for j in range(-cover, cover + 1):
                if abs(i) + abs(j) <= cover:
                    if 1 <= vx+i < 11 and 1 <= vy+j < 11:
                        if field[vx+i][vy+j] != 0:
                            field[vx+i][vy+j] = list(field[vx+i][vy+j], power)

                        else:
                            field[vx+i][vy+j] = power
    # print(field)

    # a 는 1, 1 에서 출발하고 b 는 10, 10 에서 출발한다
    # 0, 0   //   9, 9
    pos_field[1][1] = 'a'
    pos_field[10][10] = 'b'
    ay, ax = (1, 1)
    by, bx = (10, 10)
    a_battery = field[ax][ay]
    b_battery = field[bx][by]

    # range(1, M+1) 동안 이동한다.
    for t in range(M):
        
        adx, ady = directions[a_dir[t]]
        ay, ax = ay+ady, ax+adx
        # a_battery += field[ax][ay]

            # 만약 가려는 위치가 충전소 범위 내라면 충전

        bdx, bdy = directions[b_dir[t]]
        by, bx = by+bdy, bx+bdx
        # b_battery += field[bx][by]

        if ax == bx and ay == by:
            if type(field[ax][ay]) == int:
                a_battery += field[ax][ay]//2
                b_battery += field[bx][by]//2
            else:
                a_battery += max(field[ax][ay])
                b_battery += max(field[bx][by])
        else:
            if type(field[ax][ay]) == int:
                a_battery += field[ax][ay]
            else:
                if field[bx][by] == max(field[ax][ay]):
                    field[ax][ay].remove(field[bx][by])
                    a_battery += max(field[ax][ay])
                    field[ax][ay].append(field[bx][by])
            if type(field[bx][by]) == int:
                b_battery += field[bx][by]
            else:
                if field[ax][ay] == max(field[bx][by]):
                    field[bx][by].remove(field[ax][ay])
                    b_battery += max(field[bx][by])
                    field[bx][by].append(field[ax][ay])
                
    print(f'#{test_case} {a_battery + b_battery}')
            

    # 할 일
    # 1. 배터리 겹치는 구역 리스트화!! 됐꼬
    # 1. 역장이 두개 이상이면 큰거 쓰기
    # 2. 사용자 위치 겹치고 역장 하나일때 나눠쓰기