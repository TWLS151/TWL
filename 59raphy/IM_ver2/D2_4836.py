import sys

sys.stdin = open('input_4836.txt')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    square = [list(map(int, input().split())) for _ in range(N)]

    red = set()
    blue = set()

    for i in range(N):
        if square[i][4] == 1:
            for r in range(square[i][0], square[i][2]+1):
                for c in range(square[i][1], square[i][3]+1):
                    red.add((r, c))
        elif square[i][4] == 2:
            for r in range(square[i][0], square[i][2]+1):
                for c in range(square[i][1], square[i][3]+1):
                    blue.add((r, c))

    print(f'#{test_case} {len(red & blue)}')
