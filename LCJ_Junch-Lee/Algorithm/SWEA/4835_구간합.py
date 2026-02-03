
import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for T in range(1, T+1):

    # 0. SWEA 입력
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    # 1. 부분합의 최대, 최소 초기값 지정

    min_arr = sum(arr[0:M])
    max_arr = sum(arr[0:M])

    # 2. 시작점을 지정하며 M 만큼의 부분합 계산
    for start in range(N-M+1):

        arr_sum = sum(arr[start:start+M])

    # 3. M 범위의 부분합 최대, 최소 경신

        if max_arr < arr_sum:
            max_arr = arr_sum

        elif min_arr > arr_sum:
            min_arr = arr_sum


    print(f"#{T} {max_arr-min_arr}")