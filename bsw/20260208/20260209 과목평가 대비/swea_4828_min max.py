import sys

sys.stdin = open('swea_4828_min max.txt')
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    num_lst = list(map(int, input().split()))
    max_val = num_lst[0]
    min_val = num_lst[0]
    for i in range(N):
        if max_val < num_lst[i]:
            max_val = num_lst[i]
        if min_val > num_lst[i]:
            min_val = num_lst[i]
    
    print(f'#{tc} {max_val - min_val}')