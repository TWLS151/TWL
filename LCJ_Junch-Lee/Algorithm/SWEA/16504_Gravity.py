import sys

sys.stdin = open('./input.txt', 'r')

T = int(input())

def max_drop(arr, N):

    max_height = 0                  # 최대 낙차 초기값

    for idx in range(N):            # 모든 건물을 순회
        height = 0                  # 낙차 초기화

        for j in range(idx + 1, N): # 자신의 오른쪽에 있는 건물들을 탐색
            if arr[idx] > arr[j]:   # 만약 오른쪽의 건물 높이가 낮다면
                height += 1         # 낙차를 1 증가

        if max_height < height:     # height가 최대 낙차보다 크면
            max_height = height     # 최대 낙차를 갱신

    return max_height


for tc in range(1, T+1):

    N = int(input())
    arr = list(map(int, input().split()))

    result = max_drop(arr, N)

    print(f"#{tc} {result}")