# SWEA - 2382
# 미생물 격리
# 1942 / 2115

import sys
sys.stdin = open('seperate_ameba.txt')

# 미생물은 지정된 방향으로 한 시간에 한 칸씩 이동하고
# 경계에 닿으면 (n - 1) 그 수가 2로 나눈 몫 만큼 남는다
# 따라서 한 마리가 경계에 닿으면 군집이 사라진다.
# 이동 후 군집끼리 닿으면 둘이 합쳐진다.
# 합쳐지면 이동방향은 미생물 수가 많았던 군집의 방향이 된다.
# 미생물의 수가 같은 경우는 없다.
# 경계에 닿으면 이동 방향은 반대가 된다.
# 이동이 완료되었을 때 위치가 같으면 합쳐진다. 이동 도중은 고려하지 않는다.

# 0 배열을 만들고 배열에 딕셔너리를 매기면 되지 않을까?
# 딕셔너리 하나 하고 배열에 키 먹이면 될 거 같은데
# 경계에 들어가면 방향 바꾸고..
# key: ['dirs', 'nums'] 로 가볼까 그럼
# dict[key][0] = 방향
# dict[key][1] = 미생물 수
# 위치가 알파벳으로 주어지는 줄 알았는데 그냥 좌표만 주어지는구나
# 그럼 딕셔너리는 못 쓸 것 같고 그냥 좌표에다가 방향이랑 숫자 리스트를 박아야겠다.
# 근데 그러면 삼중 리스트가 되는데..
# 일단 해볼까

dirs = [0, 
    (0, 1), (-1, 0), (1, 0), (0, -1)
] # 문제에서 우상하좌 순으로 제시
# 1이 우라서 그냥 더미 0 하나 앞에 추가

TC = int(input())

for test_case in range(1, TC+1):
    pass
    size, time, zerg = map(int, input().split())
    matrix = [[0] * size for _ in range(size)]
    
    position = []
    for ameba in range(zerg):
        row, col, num, direction = map(int, input().split())
        position.append((row, col))
        matrix[row][col] = [direction, num] 


    count = 0
    # 다중 객체를 시뮬레이션 할 떄는 포지션을 절대 인덱스로 받아야 하는 것 같다.
    for t in range(1, time+1):
        # for row, col in position:
        count = 0
        for pos in range(len(position)):
            # 이렇게 꺼내오면 나중에 위치가 변했을 때 갱신하기가 편하다
            row, col = position[pos - count]
            # [0]이 방향 [1]이 숫자
            dr, dc = dirs[matrix[row][col][0]]
            nr, nc = row + dr, col + dc
            if nr == 0 or nr == size-1 or nc == 0 or nc == size-1:
                matrix[row][col][1] //= 2
                dr, dc = dirs[matrix[row][col][0]]
                matrix[row][col][0] = dirs.index((-dr, -dc)) 

            # 경계에 닿는 걸 먼저 처리해야하나본데
            # 경계 범위는 어떻게 되지?
            # 일단 row = 0, col = 0
            # row = size-1 col = size-1
            # 이렇게네
            # 이 안에 들어가면 방향 반대고 수 // 2
            # if nr == 0 or nr == size-1 or nc == 0 or nc == size-1:
            #     # 일단 수 절반
            #     # 이동하기 전에 줄여야겠다
            #     # matrix[nr][nc][1] //= 2
            #     matrix[row][col][1] //= 2
            #     # 이제 방향
            #     # matrix[nr][nc][0] = (matrix[nr][nc][0] + 2) %4 + 1
            #     # 그냥 음수 먹이면 되네
            #     # matrix[nr][nc][0] = -matrix[nr][nc][0]
            #     # 반대됐다.
            #     # 안된다.
            #     # 그냥 분기를 두개로 나누자 # 귀찮아 # 언패킹해서 음수 먹여
            #     dr, dc = dirs[matrix[row][col][0]]
            #     # 이렇게 가면 어떤데?
            #     dirs[matrix[nr][nc][0]] = dirs.index((-dr, -dc))

            # 이동하며 숫자 이동
            # 이동한 자리에 다른 군집이 있는지도 봐야하네, 추가하자
            if matrix[nr][nc] == 0:
                matrix[nr][nc] = matrix[row][col]
                
                # 경계 처리를 여기다가 해야하네
                # if nr == 0 or nr == size-1 or nc == 0 or nc == size-1:
                #     matrix[nr][nc][1] //= 2
                #     dr, dc = dirs[matrix[row][col][0]]
                #     matrix[nr][nc][0] = dirs.index((-dr, -dc)) 

                # 원래 있던 자리 숫자 0
                position[pos - count] = (nr, nc)
                matrix[row][col] = 0
                
                if (row, col) in position:
                    position.remove((row, col))
                    count += 1
                    
            else: # 이미 다른 군집이 있으면 합쳐야해
                # 숫자 비교부터 해야겠네
                # 숫자는 합치고 방향은 더 큰쪽 방향으로
                    # 여기서 처리하면 되네.
                    # 이미 군집이 있으면 포지션에도 좌표가 있어야하는데..
                    # 이동해서 온거면 없어도 되는구나
                    # 와 미치겠네
                    # 이동 표시도 해야하나본데  # 그냥 움직일때마다 위치를 갱신하는게 낫다


                if matrix[nr][nc][1] < matrix[row][col][1]:
                    matrix[nr][nc][1] += matrix[row][col][1]
                    matrix[nr][nc][0] = matrix[row][col][0]
                else:
                    # else 처리 필요한가? 필요하네
                    matrix[nr][nc][1] += matrix[row][col][1]
                    # 방향은 그대로
                position[pos - count] = (nr, nc)
                if (row, col) in position:
                    position.remove((row, col))
                    count += 1

                # 다짰나?
    # nums =    # 지금 위치가 갱신이 안되고 있잖아?
                # 포지션 값이 계속 그대일 것 같은데
                # after_position 을 하나 만들까
                # 그리고 포지션 불러올때마다 갱신
    # time for문 끝나면 숫자 다 종합을 해야하는뎅
    total = 0
    for row in range(size):
        for col in range(size):
            if matrix[row][col] == 0:
                continue
            else:
                total += matrix[row][col][1]

    print(f'#{test_case} {total}')








# ---------------------- backup ----------------------------- #

# dirs = [0, 
#     (0, 1), (-1, 0), (1, 0), (0, -1)
# ] # 문제에서 우상하좌 순으로 제시
# # 1이 우라서 그냥 더미 0 하나 앞에 추가

# TC = int(input())

# for test_case in range(1, TC+1):
#     pass
#     size, time, zerg = map(int, input().split())
#     matrix = [[0] * size for _ in range(size)]
    
#     position = []
#     for ameba in range(zerg):
#         row, col, num, direction = map(int, input().split())
#         position.append((row, col))
#         matrix[row][col] = [direction, num, False] # 이동 여부 표시

#     after_position = position
#     # print(after_position)
#     for t in range(1, time+1):
#         position = after_position
#         for row, col in position:
#             # [0]이 방향 [1]이 숫자
#             dr, dc = dirs[matrix[row][col][0]]
#             nr, nc = row + dr, col + dc

#             # 경계에 닿는 걸 먼저 처리해야하나본데
#             # 경계 범위는 어떻게 되지?
#             # 일단 row = 0, col = 0
#             # row = size-1 col = size-1
#             # 이렇게네
#             # 이 안에 들어가면 방향 반대고 수 // 2
#             # if nr == 0 or nr == size-1 or nc == 0 or nc == size-1:
#             #     # 일단 수 절반
#             #     # 이동하기 전에 줄여야겠다
#             #     # matrix[nr][nc][1] //= 2
#             #     matrix[row][col][1] //= 2
#             #     # 이제 방향
#             #     # matrix[nr][nc][0] = (matrix[nr][nc][0] + 2) %4 + 1
#             #     # 그냥 음수 먹이면 되네
#             #     # matrix[nr][nc][0] = -matrix[nr][nc][0]
#             #     # 반대됐다.
#             #     # 안된다.
#             #     # 그냥 분기를 두개로 나누자 # 귀찮아 # 언패킹해서 음수 먹여
#             #     dr, dc = dirs[matrix[row][col][0]]
#             #     # 이렇게 가면 어떤데?
#             #     dirs[matrix[nr][nc][0]] = dirs.index((-dr, -dc))

#             # 이동하며 숫자 이동
#             # 이동한 자리에 다른 군집이 있는지도 봐야하네, 추가하자
#             if matrix[nr][nc] == 0:
#                 matrix[nr][nc] = matrix[row][col]
#                 matrix[nr][nc][2] = True # 이동 표시
#                 # 경계 처리를 여기다가 해야하네
#                 if nr == 0 or nr == size-1 or nc == 0 or nc == size-1:
#                     matrix[nr][nc][1] //= 2
#                     dr, dc = dirs[matrix[row][col][0]]
#                     matrix[nr][nc][0] = dirs.index((-dr, -dc)) 

#                 # 원래 있던 자리 숫자 0
#                 if matrix[row][col][2] == False:
#                     position.remove((row, col))
#                 matrix[row][col] = 0
                
#             else: # 이미 다른 군집이 있으면 합쳐야해
#                 # 숫자 비교부터 해야겠네
#                 # 숫자는 합치고 방향은 더 큰쪽 방향으로
#                     # 여기서 처리하면 되네.
#                     # 이미 군집이 있으면 포지션에도 좌표가 있어야하는데..
#                     # 이동해서 온거면 없어도 되는구나
#                     # 와 미치겠네
#                     # 이동 표시도 해야하나본데
#                 if matrix[nr][nc][2] == False:
#                     position.remove((nr, nc))
#                 if matrix[nr][nc][1] < matrix[row][col][1]:
#                     matrix[nr][nc][1] += matrix[row][col][1]
#                     matrix[nr][nc][0] = matrix[row][col][0]
#                 else:
#                     # else 처리 필요한가? 필요하네
#                     matrix[nr][nc][1] += matrix[row][col][1]
#                     # 방향은 그대로
#                 matrix[nr][nc][2] = True
#             # position.pop
#             after_position.append((nr, nc))
#             # after_position.remove((row, col))
#             after_position.pop(0)
                
#                 # 다짰나?
#     # nums =    # 지금 위치가 갱신이 안되고 있잖아?
#                 # 포지션 값이 계속 그대일 것 같은데
#                 # after_position 을 하나 만들까
#                 # 그리고 포지션 불러올때마다 갱신
#     # time for문 끝나면 숫자 다 종합을 해야하는뎅
#     total = 0
#     for row in range(size):
#         for col in range(size):
#             if matrix[row][col] == 0:
#                 continue
#             else:
#                 total += matrix[row][col][1]

#     print(f'#{test_case} {total}')

