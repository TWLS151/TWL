import sys

sys.stdin = open('./input.txt', 'r')

T = int(input())

def selecting_sort(arr, N):

    # 외부 for : 정렬된 값이 들어올 기준점
    for idx in range(N-1):

        min_idx = idx # 현재 위치를 기준점으로 설정

        for j in range(idx + 1, N): # 기준점보다 앞의 값 ~ 끝값에 대해 순회

            if arr[min_idx] > arr[j]: # 현재 최소값보다 작은 값 발견 시
                min_idx = j          # 인덱스 수정

        arr[idx], arr[min_idx] = arr[min_idx], arr[idx]

    return arr  # 정렬완료 후, 정렬된 리스트 반환

for tc in range(1, T+1):

    # 리스트 길이, 리스트를 입력
    N = int(input())
    arr = list(map(int, input().split()))

    result = selecting_sort(arr, N)

    print(f"#{tc}", *result, sep=' ')

