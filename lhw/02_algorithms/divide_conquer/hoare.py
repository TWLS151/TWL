# import sys

# sys.stdin = open('input.txt')


def quick_sort_hoare(arr, start, end):
    """
    호어 파티션 기반의 퀵 정렬 매니저 함수입니다.
    """
    if start < end:
        # 1. 분할: 파티션을 수행하고 분할 기준점(pivot_idx)을 받습니다.
        pivot_idx = partition_hoare(arr, start, end)

        # 2. 정복: 분할 기준점의 좌우를 각각 재귀 호출합니다.
        quick_sort_hoare(arr, start, pivot_idx - 1)
        quick_sort_hoare(arr, pivot_idx + 1, end)


def partition_hoare(arr, start, end):
    """
    호어 파티션: 가장 왼쪽 원소를 피벗으로 사용하고, 투 포인터로 교환을 진행합니다.
    """
    pivot = arr[start]
    left = start + 1
    right = end

    # left와 right 포인터가 교차하기 전까지 반복합니다.
    while left <= right:
        # left 포인터 이동: 피벗보다 큰 값을 찾을 때까지 오른쪽으로 이동합니다.
        while left <= end and arr[left] <= pivot:
            left += 1
        # right 포인터 이동: 피벗보다 작은 값을 찾을 때까지 왼쪽으로 이동합니다.
        while right > start and arr[right] >= pivot:
            right -= 1

        # 만약 포인터가 교차했다면, 분할 작업이 거의 끝난 것입니다.
        if left > right:
            # 피벗(arr[start])을 분할 기준점(arr[right])과 교환합니다.
            arr[start], arr[right] = arr[right], arr[start]
        # 아직 교차 전이라면, left와 right가 가리키는 값을 서로 교환합니다.
        else:
            arr[left], arr[right] = arr[right], arr[left]

    # 피벗의 최종 위치인 right를 반환합니다.
    return right


T = int(input())
for tc in range(1, T + 1):
    numbers = list(map(int, input().split()))
    quick_sort_hoare(numbers, 0, len(numbers) - 1)
    print(f'#{tc}', *numbers)
