def bubble_sort(a, N):
    for i in range(N-1, 0, -1):
        for j in range (i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

arr = [64, 11, 22, 10, 53]
len = 5
result = bubble_sort(arr, len)
print(result)