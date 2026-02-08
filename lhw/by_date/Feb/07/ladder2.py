# SWEA - 1211
# LADDER 2
# TTP: 52'44"

import sys
sys.stdin = open('ladder2.txt')

TC = 10

for test_case in range(1, TC+1):
    test_num = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    pass

    # 아래로 가는게 우선
    # 전에 못쓴 방향표시를 써볼까
    # head = {
    #     'v': (1, 0),
    #     '<': (0, -1),
    #     '>': (0, 1)
    # }

    min_count = 10**99
    for col in range(100):
        row = 0
				# 1 찾으면 돌입
        if ladder[row][col] == 1:
            count = 0
            # heading = head['v']
            position = (row, col)
            px, py = position

        while px + 1 < 100:
            px += 1
            count += 1
						# 오른쪽으로 이동
            if py + 1 < 100 and ladder[px][py+1] == 1:
                while py + 1 < 100 and ladder[px][py+1] == 1:
                    py += 1
                    count += 1
            # 왼쪽으로 이동
            elif 0 <= py - 1 and ladder[px][py-1] == 1:
                while py -1 >= 0 and ladder[px][py-1] == 1:
                    py -= 1
                    count += 1
            
        if min_count > count:
            min_count = count
            min_col = col
        
    print(f'#{test_case} {min_col}')
