import sys

sys.stdin = open('swea_4843_특별한 정렬.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    n_lst = list(map(int, input().split()))
    result = []
    for i in range(5):
        result.append(n_lst.pop())
        result.append(n_lst.pop(0))
    print(f'#{tc}', *result)