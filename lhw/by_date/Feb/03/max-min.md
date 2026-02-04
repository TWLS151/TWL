# SWEA - 11092
## 최대 최소의 간격

- 최댓값은 가장 끝에 있는걸 쓰고 최솟값은 가장 앞에 있는걸 쓰니까 두 개의 청크를 만들었는데 솔루션을 보니 그럴 필요가 없었습니다.

- 마음이 아픕니다.. 오늘은 왜인지 enumerate에 꽂혀서 계속 생각이 났습니다..

# Solution
```python
# 2. 배열 순회 및 인덱스 갱신
    # 배열의 모든 원소를 확인하기 위해 0부터 N-1까지 순회합니다.
    for i in range(N):
        # 2-1. 최대값 인덱스 찾기
        # 현재까지의 최대값(arr[max_index])이 현재 원소(arr[i])보다 '작거나 같으면'
        # max_index를 현재 인덱스(i)로 갱신합니다.
        # '같을 때도' 갱신하는 이유는 문제의 조건인
        # "최대값이 여러 개일 경우 가장 뒤에 있는 인덱스"를 찾기 위함입니다.
        if arr[max_index] <= arr[i]:
            max_index = i

        # 2-2. 최소값 인덱스 찾기
        # 현재까지의 최소값(arr[min_index])이 현재 원소(arr[i])보다 '크면'
        # min_index를 현재 인덱스(i)로 갱신합니다.
        # '클 때만' 갱신하는 이유는 문제의 조건인
        # "최소값이 여러 개일 경우 가장 앞에 있는 인덱스"를 유지하기 위함입니다.
        if arr[min_index] > arr[i]:
            min_index = i
```


```python
# 본 코드

TC = int(input())

for test_case in range(1, TC + 1):
    N = int(input())
    num_lst = list(map(int, input().split()))
    
    # 인덱스 변수 설정
    max_idx = min_idx = -1

    # 최솟값은 가장 앞에 있는걸 취하기 때문에 index 메서드 활용
    min_idx = num_lst.index(min(num_lst))

    # 최댓값은 가장 뒤에 있는걸 가져오니 for문 사용해 끝까지 탐색
    # 최댓값을 만나면 그 값의 인덱스 추출
    for k, v in enumerate(num_lst):
        if v == max(num_lst):
            max_idx = k

    # 출력
    print(f'#{test_case} {abs(max_idx - min_idx)}')
```