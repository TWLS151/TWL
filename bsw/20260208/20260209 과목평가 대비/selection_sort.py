def selection_sort(a, N):
    for i in range(N-1):
        min_idx = i
        for j in range(i+1, N):
            if a[min_idx] > a[j]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

num_lst = [64, 11, 55, 22, 10]
len = 5
print(selection_sort(num_lst, len))