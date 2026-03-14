# BOJ-14499
# 주사위 굴리기
# SW 기출 달리기 // GOLD IV

N, M, R, C, K = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(N)]
move_order = list(map(int, input().split()))

# 이동 할 때마다 주사위 윗면에 적힌 수를 출력해라.
# 처음엔 전부 0
# 주사위를 굴리는걸 어떻게 구현하지 ..

# 두 개의 리스트가 나오네
# 축이 바뀌면 리스트가 바뀐다.

dirs = [
    0, (0, 1), (0, -1), (-1, 0), (1, 0)
]

# TOP 0, BOTTOM 1, NORTH 2, SOUTH 3, EAST 4, WEST 5
dice = [0, 0, 0, 0, 0, 0]

def roll(cmd):
    global dice

    pdice = dice[:]
    if cmd == 1:
        dice[0] = pdice[4]
        dice[1] = pdice[5]
        dice[2] = pdice[2]
        dice[3] = pdice[3]
        dice[4] = pdice[1]
        dice[5] = pdice[0]
    
    elif cmd == 2:
        dice[0] = pdice[5]
        dice[1] = pdice[4]
        dice[2] = pdice[2]
        dice[3] = pdice[3]
        dice[4] = pdice[0]
        dice[5] = pdice[1]
    
    elif cmd == 3:
        dice[0] = pdice[3]
        dice[1] = pdice[2]
        dice[2] = pdice[0]
        dice[3] = pdice[1]
        dice[4] = pdice[4]
        dice[5] = pdice[5]
    
    else:
        dice[0] = pdice[2]
        dice[1] = pdice[3]
        dice[2] = pdice[1]
        dice[3] = pdice[0]
        dice[4] = pdice[4]
        dice[5] = pdice[5]
    
pos = (R, C)
for order in move_order:
    
    dr, dc = dirs[order]
    nr, nc = R+dr, C+dc

    if not (0 <= nr < N and 0 <= nc < M):
        continue


    R, C = nr, nc
    roll(order)

    if field[nr][nc] == 0:
        field[nr][nc] = dice[1]
        # dice[1] = 0
    else:
        dice[1] = field[nr][nc]
        field[nr][nc] = 0
    

    print(dice[0])
