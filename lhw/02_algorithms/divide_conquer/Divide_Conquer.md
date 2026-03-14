# 분할정복

### 1. Quick - Sorting

1. 원리
    1. Divide :  
    리스트 내에서 기준점, `Pivot point`를 하나 정하고 이 후 기준점보다 작은 값을 왼쪽으로, 큰 값을 오른쪽으로 나누는 **파티션**, `Partition` 작업을 수행
    2. Conquer :  
    둘로 나뉜 각 파트에서 다시 `Pivot`을 정하고 다시 `Partition` 을 수행
    3. Combine :  
    `Partition`을 통해 정렬이 완료되었으니 재귀 깊이가 끝에 도달하면 정렬이 끝난다.  

2. 로무토
   
   1. 코드
      ```python
      def quick_sort_lomuto(arr, start, end):
        if start < end:
          pivot_idx = partition_lomuto(arr, start, end)

        quick_sort_lomuto(arr, start, pivot_idx-1)
        quick_sort_lomuto(arr, pivot_idx+1, end)

      def partition_lomuto(arr, start, end):
        pivot = arr[end]
        # [1] 피벗 왼쪽 파티션의 경계
        i = start-1

        for j in range(start, end):
          if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

        arr[i+1], arr[end] = arr[end], arr[i+1]

        return i + 1
      ```
      로무토는 파티션의 가장 오른쪽 값을 기준값으로 사용하는 방식  
      `# [1]`의 `i = start-1` 코드가 중요한데, 파티션 내에서 정렬이 끝났을 때 기준점이 들어갈 위치를 정한다. ( `return i + 1` )

2. 호어

   1. 코드
      ```python
      def quick_sort_hoare(arr, start, end):
        if start < end:
          pivot_idx = partition_hoare(arr, start, end)

          quick_sort_hoare(arr, start, pivot_idx - 1)
          quick_sort_hoare(arr, pivot_idx + 1, end)

      def partition_hoare(arr, start, end):
        pivot = arr[start]
        left = start + 1
        right = end

        while left <= right:
          while left <= end and arr[left] <= pivot:
            left += 1
          
          while right <= end and arr[right] >= pivot:
            right += 1
          
          if left > right:
            arr[start], arr[right] = arr[right], arr[start]
          else:
            arr[left], arr[right] = arr[right], arr[left]
        
        return right
      ```
      호어는 파티션의 가장 왼쪽 값을 기준 값으로 사용하는 방식  
      포인터를 사용해 정렬을 진행한다.


'''
호어 진행 | arr = [5, 4, 6, 2, 1]
5, 4, 6, 2, 1 | start = 0, left = 1, right = 4

Partition 함수 진입 후 포인터 확정
start = 0, left = 2, right = 4
left < right 이므로 둘 교환

교환 후
arr = [5, 4, 1, 2, 6] | start = 0, left = 2, right = 4

교차하지 않았으니 다시 진행
포인터 확정
start = 0, left = 4, right = 3
left > right 이므로 pivot 변경, right == 3 반환

변경 후
arr = [2, 4, 1, 5, 6]

Partition 함수 재진입
[1]
arr = [2, 4, 1, 5, 6] | start = 0, left = 1, right = 2
[2]
arr = [2, 4, 1, 5, 6] | start = 4, left = 5, right = 4

# [1]
포인터 확정
start = 0, left = 1, right = 2
left < right
arr = [2, 1, 4, 5, 6]

반복 진행 후 포인터 확정
start = 0, left = 2, right = 1
left > right | pivot 변경
arr = [1, 2, 4, 5, 6] | right ==1 반환

# [2]
left > right | right 4 반환 후 함수 종료

정렬 완료
arr = [1, 2, 4, 5, 6]
'''