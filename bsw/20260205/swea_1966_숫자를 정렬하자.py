def selection_sort(a, N):
    for i in range(N-1):
        min_idx = i
        for j in range(i+1, N):
            if a[min_idx] > a[j]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

def bubble_sort(b, M):
    for i in range(M-1, 0, -1):
        for j in range(i):
            if b[j] > b[j+1]:
                b[j], b[j+1] = b[j+1], b[j]
    return b

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))
    num_lst = selection_sort(data, N)
    print(f'#{tc}', *num_lst)
