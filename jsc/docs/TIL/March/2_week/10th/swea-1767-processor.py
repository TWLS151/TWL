import sys

sys.stdin = open("111.txt")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    print(board)
