import sys
sys.stdin = open('swea-1209.txt')

T = int(input())

for tc in range(1, T+1):
    board = [list(map(int, input().split())) for _ in range(100)]

    max_val = float('-inf')
    val = 0
    diagnol_sum = 0
    anti_diagnol_sum = 0

    for row in range(0,100):
        val = sum(board[row])
        max_val = max(max_val, val)


    zip_board = list(zip(*board))
    for row in range(0,100):
        val = sum(zip_board[row])
        max_val = max(max_val, val)

    for num in range(100):
        diagnol_sum += board[num][num]
        anti_diagnol_sum += board[num][99-num]

    max_val = max(max_val, diagnol_sum, anti_diagnol_sum)
    print(max_val)