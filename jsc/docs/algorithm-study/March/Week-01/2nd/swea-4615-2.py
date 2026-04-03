'''
시뮬레이션 문제이다. 
돌을 놓은 이후에 어디를 체크를 할 것인가
일단 빈 격자를 만들어야한다.
빈 격자를 만든다.
여기에 M을 이용을 해서 돌을 놓는다.
돌을 놓을 때 마다 상하좌우대각선을 확인을 한다.
딸 수 있는 돌이 있으면 내 돌로 바꾼다.
숫자를 셀 필요는 없다.
주어지는 데이터의 타입은 막 크지는 않는 것 같다.
그냥 케이스 하나네??

범위를 잡을 때 
if board[nr][nc] == -1 or not (1 <= nr <= N and 1 <= nc <= N):
#        break
이렇게 놓으면 안된다. 왜냐하면 or문은 앞에 있는것을 먼저 처리를 하기 때문에 값을 확인을 하다가 인덱스 에러를 발생을
시킬 수 있기 때문이다. 범위를 먼저 확인을 하고 값을 확인을 해야한다.
'''


import sys
sys.stdin = open('swea-4615.txt')

# Making the default board
def setting(N, M):
    board = [[-1] * (N+1)] + [[-1] + [0] * N for _ in range(N)]
    mid = N // 2
    board[mid][mid] = 1
    board[mid][mid + 1] = 2
    board[mid + 1][mid] = 2
    board[mid + 1][mid + 1] = 1
    return board
    pass

def put_stone(board, r, c, color):
    board[r][c] = color
    return board

def flip_recursive(r, c, dr, dc, color, board, N):
    nr, nc = r + dr, c + dc
    
    if not (1 <= nr <= N and 1 <= nc <= N) or board[nr][nc] == 0:
        return False

    if board[nr][nc] == color:
        return True
    
    if flip_recursive(nr, nc, dr, dc, color, board, N):
        board[nr][nc] = color
        return True
    
    return False

def flip_stone(board, cr, cc, color, N):
    dr = [-1, -1, 0, 1, 1, 1, 0, -1]
    dc = [0, 1, 1, 1, 0, -1, -1, -1]

    for i in range(8):
        flip_recursive(cr, cc, dr[i], dc[i], color, board, N)

    return board
# Check the white and black stones on the board, after whole tasks
def check(board):
    white_cnt = 0
    black_cnt = 0
    for r in range(1, N+1):
        for c in range(1, N+1):
            if board[r][c] == 2:
                white_cnt += 1
            if board[r][c] == 1:
                black_cnt += 1

    return white_cnt, black_cnt
    pass


# === start of code
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    
    # board setting
    # index[0] -> -1
    basic_board = setting(N, M)
    put_board = basic_board

    for _ in range (M):
        r, c, color = map(int, input().split())

        # put the stones
        put_board = put_stone(put_board, r, c, color)
        fliped_board = flip_stone(put_board, r, c, color, N)
        
    white, black = check(fliped_board)
    print(black, white)
        


