'''
이진 탐색(Binary search) 실습 코드
'''
arr = [7, 4, 2, 9, 11, 23, 19]

arr.sort()


def binary_search_while(target):

    left = 0                # 검색 시작점
    right = len(arr) - 1 # 검색 끝점


    # 정답을 못 찾았을 경우에는? 
    # right가 어느 순간 left, mid와 교차되는(왼쪽으로 가는) 순간 존재
    while left <= right :

        mid = (left + right) // 2

        if arr[mid] == target:   # 정답을 찾으면 종료
            return mid
        
        # arr[mid]가 target보다 더 큰 경우 (왼쪽 탐색)

        if arr[mid] > target:
            right = mid - 1

        # arr[mid]가 target보다 작은 경우 (오른쪽 탐색)

        if arr[mid] < target:
            left = mid + 1
    
    return -1


targets = [9, 2, 20]

for target in targets:

    result = binary_search_while(target)

    if result == -1:
        print(f"{target}은 배열에 없습니다.")

    else:
        print(f"{target}은 {result} 인덱스에 있습니다.")