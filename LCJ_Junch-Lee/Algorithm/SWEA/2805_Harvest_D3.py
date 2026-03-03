import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

'''
풀이 접근 흐름

1. 중앙 인덱스의 행, 열은 반드시 수확영역에 포함된다.

2. 더해주면 안되는 영역의 값을 다 0으로 만들면 어떨까? 

- 규칙성이 존재한다.
- row1(i=0) : range(N//2) : arr[행][i] = arr[행][N-1-i] = 0
- row2(i=1) : range(N//2 - 1) : 동일
- row3(i=2) : range(N//2 - 2) : 동일
- row4(i=3) : skip

## 여기서부터 데칼코마니인데, 어떻게 구현해줄 수 있을까?
# Hint
# goal : 3 2 1 0 1 2 3 ??? 
# row  : 0 1 2 3 4 5 6

- row5(i=4) : range(1) 0, 6
- row6(i=5) : range(2) 0-6, 1-5
- row7(i=6) : range(3) 0-6, 1-5, 2-4

5x5 = 3,4 -> 1,2
7x7 = 4,5,6 -> 1,2,3
'''

def do_harvest(arr, N):

    total = 0
    
    for r in range(N//2):               # 위 절반 - 1 행에 대해
        for c in range(N//2-r):           # 절반씩만 탐색
            arr[r][c] = arr[r][N-1-c] = 0 # 마름모를 벗어난 영역을 0으로 만듦


    for r in range(N//2 + 1, N):            # 아래 절반 + 1 행에 대해
        for c in range(r - N//2):           # 동일하게 깎아내기
            arr[r][c] = arr[r][N-1-c] = 0 
    
    for row in arr:
        total += sum(row)


    return total

for tc in range(1, T+1):

    N = int(input())

    arr = [list(map(int, input())) for _ in range(N)]

    result= do_harvest(arr, N)

    print(f"#{tc} {result}")
