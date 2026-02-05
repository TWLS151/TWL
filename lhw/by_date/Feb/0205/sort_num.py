# SWEA - 1966

# 선택정렬로 풀어보자

def selection(arr):
    N = len(arr)

    for idx in range(N - 1):
        min_idx = idx

        for i in range(idx+1, N):
            if arr[min_idx] > arr[i]:
                min_idx = i
        
        arr[idx], arr[min_idx] = arr[min_idx], arr[idx]

tc = int(input())

for test_case in range(1, tc+1):
    N = int(input())
    lst = list(map(int, input().split()))

    selection(lst)

    print(f'#{test_case}', *lst)