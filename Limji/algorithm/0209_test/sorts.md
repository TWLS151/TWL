## bubble sort
- 첫 번째 원소부터 인접한 두 개의 원소끼리 비교하며 계속 자리를 교환하는 방식(내부 반복)으로, 외부 반복 기준 한 단계가 끝나면 가장 큰 원소가 마지막 자리로 정렬된다.
- 시간 복잡도 : $O(n^2)$
- 장점 | 제자리 정렬(In-place Sort) : 추가 메모리 공간 거의 필요 X.
- 단점 | 대용량 데이터 부적합, 데이터 개수(n)이 늘어날 수록 계산량이 제곱으로 늘어난다.

<br>

- 외부 반복 | 정렬 범위를 뒤에서부터 줄여나간다
- 내부 반복 | `0`부터 `i+1`까지 인접한 원소끼리 비교를 반복한다. (`i` 이후 뒷부분은 이미 정렬 완료 상태이므로 무시)
- 교환 | 앞의 원소`j`가 뒤의 원소`j+1`보다 크다면 교환한다.

### [basic] python code 
```python
def bubble_sort(arr):
    n = len(arr)

    # [외부 반복] 정렬 범위를 뒤에서부터 하나씩 줄여나갑니다.
    # range(n-1, 0, -1): n-1부터 1까지 역순으로 반복
    for i in range(n - 1, 0, -1):

        # [내부 반복] 0부터 i-1까지 인접한 원소를 비교합니다.
        # i 이후의 뒷부분은 이미 정렬이 완료된 상태이므로 비교할 필요가 없습니다.
        for j in range(i):

            # [비교 및 교환] 앞의 원소가 뒤의 원소보다 크다면?
            # 작다면? 아래 부등호만 반대로 하기
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap

    return arr

# 테스트
numbers = [64, 13, 9, 62, 3] # 요소 다섯 개인 리스트를 정렬
print(f"정렬 전: {numbers}")
print(f"정렬 후: {bubble_sort(numbers)}")
```

### [advanced] python code

- Scenario: "데이터가 10,000개인데 이미 거의 다 정렬되어 있다면?"  
- Problem: 일반 버블 정렬은 무조건 1억 번($10,000^2$)에 가까운 비교를 수행한다.  
- Solution: **swapped 플래그**를 도입해, 외부 반복 기준 해당 한 회전 동안 교환이 없으면 즉시 종료한다.   
- Result: 데이터가 정렬된 상태라면 비교 횟수가 $10,000번(n)$으로 줄어들어 성능이 비약적으로 향상된다. -> 최선의 경우 $O(n)$  

```python
for i in range(N - 1, 0, -1):
    swapped = False # 매 바퀴마다 일단 자리를 바꿀 일이 없다고 가정한다.
    for j in range(i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            swapped = True  # 만약 자리를 바꿨다면 다음 것도 탐색
    # 자리를 바꾸지 않았다면 여전히 swapped = False 겠죠?
    
    if not swapped: # 한 번도 자리를 안 바꿨다면 이미 정렬 끝!
        break # 조기 퇴근!
```

## selection sort
- 전체 데이터에서 최솟값을 찾아 맨 앞부터 순서대로 정렬된 위치를 확정해나가는 알고리즘이다.
- 시간 복잡도 : $O(n^2)$
- 장점 | 구현 간단하고 직관적
- 단점 | 데이터가 정렬된 상태라도 전체를 비교해야 하므로 비효율적이고 양이 많아지면 성능 저하

- 외부 반복 | 각 단계마다 `i`번째 자리에 들어갈 값을 찾는다.
- 내부 반복 | `i+1`부터 끝까지 순회하며 가장 작은 값의 인덱스 찾는다.
- 교환 | 내부 반복이 끝나면, 찾은 최솟값`arr[min_idx]`을 정렬이 필요한 현재 위치`arr[i]`와 맞바꾼다.

### [basic] python code
```python
def selection_sort(arr):
    """
    선택 정렬 (Selection Sort):
    - 매 회차마다 '남은 구간'에서 최솟값을 '선택'하여 정해진 위치로 옮기는 방식
    - 시간 복잡도: O(n^2)
    """
    n = len(arr)

    # [외부 반복] 정렬할 위치(i)를 하나씩 결정해 나갑니다.
    # 마지막 원소 하나가 남았을 때는 이미 정렬된 상태이므로 n-1번만 반복합니다.
    for i in range(n - 1):

        # 1. 일단 현재 보고 있는 위치(i)를 '최솟값의 위치'라고 가정합니다.
        min_idx = i

        # 2. [내부 반복] 아직 정렬되지 않은 나머지 구간(i+1 ~ 끝)을 탐색합니다.
        for j in range(i + 1, n):
            # 현재 가정된 최솟값보다 더 작은 값을 발견하면?
            if arr[j] < arr[min_idx]:
                # "아, 얘가 진짜 최솟값이네!" 하고 위치(인덱스)를 갱신합니다.
                min_idx = j

        # 3. [교환] 탐색이 끝난 후, 진짜 최솟값(min_idx)을 현재 자리(i)로 가져옵니다.
        # (만약 min_idx와 i가 같다면 제자리 교환이 일어납니다 - 로직상 문제없음)
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


# --- 실행 및 검증 ---
numbers = [2, 5, 1, 3, 4]
print(f"정렬 전: {numbers}")

selection_sort(numbers)

print(f"정렬 후: {numbers}")

```
### [advanced] k번째로 작은 원소 구하기

```python
def selection_sort(arr, k):

    n = len(arr)

    for i in range(k):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    # k번째의 원소는 인덱스 번호 k-1번이다.
    return arr[k-1]


numbers = [2, 5, 1, 3, 4]
k = 3
print(f"정렬 전: {numbers}")

result = selection_sort(numbers, k)
print(f"정렬 후: {numbers}")
print(f"{k}번 째로 작은 원소는?:{result}")
```

## counting sort

### [basic] python code


## other sorts

| 알고리즘 | 평균 수행시간 | 최악 수행시간 | 알고리즘 기법 | 비고 |
| :--- | :--- | :--- | :--- | :--- |
| **버블 정렬** | $O(n^2)$ | $O(n^2)$ | 비교와 교환 | 코딩이 가장 손쉽다. |
| **카운팅 정렬** | $O(n+k)$ | $O(n+k)$ | 비교환 방식 | $n$이 비교적 작을 때만 가능하다. |
| **선택 정렬** | $O(n^2)$ | $O(n^2)$ | 비교와 교환 | 교환의 회수가 버블, 삽입정렬보다 작다. |
| **퀵 정렬** | $O(n \log n)$ | $O(n^2)$ | 분할 정복 | 최악의 경우 $O(n^2)$ 이지만, 평균적으로 가장 빠르다. |
| **삽입 정렬** | $O(n^2)$ | $O(n^2)$ | 비교와 교환 | $n$의 개수가 작을 때 효과적이다. |
| **병합 정렬** | $O(n \log n)$ | $O(n \log n)$ | 분할 정복 | 연결리스트의 경우 가장 효율적인 방식 |