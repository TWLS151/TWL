import sys

sys.stdin = open('input_4843.txt')

from collections import deque

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = (list(map(int, input().split())))

    numbers = deque(sorted(arr))
    sorted_num = []

    for i in range(5):
        sorted_num.append(numbers.pop())
        sorted_num.append(numbers.popleft())

    print(f'#{test_case}', *sorted_num)
