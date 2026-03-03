import sys

sys.stdin = open('./input.txt', 'r')

T = int(input())

def selecting_sort(arr, N):

    for idx in range(N-1):
        min_idx = idx

        for j in range(idx + 1, N):

            if arr[min_idx] > arr[j]:
                min_idx = j

        # 최소값 index가 min_idx에 할당된 이후

        arr[idx], arr[min_idx] = arr[min_idx], arr[idx]

    return arr

def unique_sort(arr):

    unique_arr = []

    for i in range(1,11):

        if i % 2 == 1: # 1 ~ 홀수 번의 경우
            unique_arr.append(arr.pop()) # 큰 값을 반환

        else: # 짝수 번의 경우 작은 값을 반환
            unique_arr.append(arr.pop(0))

    return unique_arr

for tc in range(1, T+1):

    N = int(input())
    arr = list(map(int, input().split()))

    # 1. 선택 정렬
    sort_arr = selecting_sort(arr, N) # 정렬된 arr 반환

    # 2. 특별한 정렬 규칙에 따라 정렬된 10개의 리스트 반환

    final_arr = unique_sort(sort_arr)

    print(f"#{tc}", *final_arr, sep = " ")