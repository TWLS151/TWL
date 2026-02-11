import sys

sys.stdin = open('swea_2805_농작물 수확하기.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    result = 0 # 결과값 지정
    center = N // 2 # 가운뎃 값
    s, e = center, center # 시작과 끝
    for i in range(N):
        for j in range(s, e + 1): # 시작과 끝 범위를 순회
            result += arr[i][j]

        if i < center: # 가운뎃 줄 전까지는 더하는 시작값을 1 줄이고 끝나는 값을 1 늘림.
            s -= 1
            e += 1
        else:
            s += 1
            e -= 1
    print(f'#{tc} {result}')



