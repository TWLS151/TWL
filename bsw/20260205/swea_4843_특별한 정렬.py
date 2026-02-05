# 빈 리스트를 추가
# 최댓값을 찾아서 빈 리스트에 append
# 최솟값을 찾아서 빈 리스트에 append
# 선택 정렬을 통해서 리스트 정렬
def selection_sort(a, N):
    for i in range(N-1):
        max_idx = i
        for j in range(i+1, N):
            if a[max_idx] < a[j]:
                max_idx = j
        a[i], a[max_idx] = a[max_idx], a[i]
    return a

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))
    reversed_data = selection_sort(data, N)
    result_data = [] # 결과 리스트를 생성
    for i in range(5):
        result_data.append(reversed_data.pop(0))
        result_data.append(reversed_data.pop())
        # 최댓값, 최솟값을 뽑고 번갈아 채우는 방식
    print(f'#{tc}',*result_data)

