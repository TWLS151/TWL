import sys

sys.stdin = open('swea_1220_magnetic.txt')

for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    dr = [-1, 1]
    count = 0
    for c in range(100): # c, r 순인데 arr[r][c]면 세로줄 검사.
        red = False
        for r in range(100):
            if arr[r][c] == 1: # c열에 1이 있다는 소리
                red = True
            elif arr[r][c] == 2: # 위에서 아래로 내려가다가 2 발견하면 카운트 올리고 초기화
                if red:
                    count += 1
                    red = False
    print(f'#{tc} {count}')



