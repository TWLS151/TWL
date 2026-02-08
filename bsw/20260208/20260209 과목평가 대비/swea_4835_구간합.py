T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    num_lst = list(map(int, input().split()))
    max_val, min_val = 0, 0
    for i in range(M):
        max_val += num_lst[i]
        min_val += num_lst[i]
    for i in range(N-M+1):
        sum_lst = 0
        for j in range(M):
            sum_lst += num_lst[i + j]
    if max_val < sum_lst:
            max_val = sum_lst
    if min_val > sum_lst:
            min_val = sum_lst
            
    print(f'#{tc} {max_val - min_val}')