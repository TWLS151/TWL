


T = int(input())
for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    charge_lst = [0] + list(map(int, input().split())) + [N]
    last_loc = 0
    count_lst = 0
    for i in range(1, len(charge_lst)):
        if charge_lst[i] - charge_lst[i-1] > K:
            count = 0
            break
        else:
            if charge_lst[i] - last_loc > K:
                count += 1
                last_loc = charge_lst[i-1]
    print(f'#{tc} {count}')



