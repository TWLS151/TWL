import sys
from collections import deque

sys.stdin = open('input.txt')

TC = int(input())

for test_case in range(1, TC+1):
    N, M = map(int, input().split())
    lst = deque(input().split())
    lst.rotate(-M)

    print(f'#{test_case} {lst[0]}')