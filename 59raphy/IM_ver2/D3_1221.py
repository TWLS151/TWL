import sys

sys.stdin = open('input_1221.txt')

T = int(input())

for test_case in range(1, T + 1):
    tc, N = input().split()
    numbers = list(input().split())
    exoplanet_num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    numbers.sort(key=lambda x: exoplanet_num.index(x))

    print(tc, *numbers)
