def special_sort(a, len):
    for i in range(10):
        target_idx = i
        if i % 2 != 0:
            for j in range(i+1, len):
                if a[target_idx] > a[j]:
                    target_idx = a[j]
        else:    
            for k in range(i+1, len):
                if a[target_idx] < a[k]:
                    target_idx = k
        a[i], a[target_idx] = a[target_idx], a[i]
    return a

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    num_lst = list(map(int, input().split()))
    result = special_sort(num_lst, N)
    print(f'#{tc}', *result)



