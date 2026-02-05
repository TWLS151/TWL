def selection_sort(arr):
    n = len(arr)
    # 0부터 n-2까지, 각 자리에 들어갈 값을 찾기 위해 반복 (마지막 인덱스 전까지만 순회)
    for i in range(n - 1):
        # 현재 자리를 최솟값의 위치로 가정
        min_idx = i

        # 현재 자리(i) 다음부터 끝까지 탐색하며 실제 최솟값 위치를 찾음
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # 찾은 최솟값을 현재 자리(i)로 보내고, 원래 있던 값은 최솟값 자리로 보냄
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


# --- 실행 코드 ---
numbers = [2, 5, 1, 3, 4]
print(f"정렬 전: {numbers}")

selection_sort(numbers)

print(f"정렬 후: {numbers}")