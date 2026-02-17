import sys

sys.stdin = open('input_4835.txt')

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    max_sum = sum(arr[0:M])
    min_sum = sum(arr[0:M])

    for i in range(N - M + 1):
        sum_m = sum(arr[i:i+M])
        if max_sum < sum_m:
            max_sum = sum_m
        elif min_sum > sum_m:
            min_sum = sum_m

    print(f'#{test_case} {max_sum - min_sum}')
