## 검색과 정렬


### 검색(Search) ?

: 저장되어 있는 자료에서 원하는 항목을 찾는 작업 

목적하는 탐색 키를 가진 항목을 찾는 것

&nbsp;

### 탐색 키 (Find Key) 

: 자료를 구별하여 인식할 수 있는 키


&nbsp;

## 순차 검색

: 일렬로 되어있는 자료를 순서대로 검색하는 방법

- 우리가 이미 많이 사용하는 탐색법.

- 배열의 존재 이유 중 하나. 

- `for idx in range(N): ~`  같은 형태를 사용

&nbsp;

## 1. 정렬되어 있지 않은 경우의 순차검색

- 첫 번째 -> 마지막 원소까지 검색 대상과 키 값이 같은 원소가 있는지 찾는다

- 키 값이 동일한 원소를 찾으면 그 원소의 인덱스를 반환 

- 마지막까지 찾지 못한다면 탐색 실패

### >>> 정렬 X의 경우, 무조건 `list`의 끝까지 탐색해야 함

구현 예시

```python
# 구현 예시 1 (while)

def sequential_search(a, n, key):

  i = 0
  while i < n and a[i] != key:
    i += 1
    if i < n:
        return i
    else:
      return -1
```

```python
def sequnetial_search(a, n, key):
  for i in range(n):
    if a[i] == key:
      return i

  else : return -1
```

&nbsp;

## 2. `list`가 정렬되어있는 경우

- 찾고자 하는 원소 순서에 따라 비교 횟수가 결정됨

- 내가 찾고자 하는 항목보다 탐색하는 인덱스의 값이 크다면, 바로 검색을 중단
  - 검색 실패를 반환하는 경우에도, 평균 비교 횟수가 반으로 줄어든다

```python
# cf. 간단한 프로그래밍은 함수화하는 연습을 해보자.

def sequential_search(arr, n, key):

  for idx in range(n):
    if arr[idx] == key:
      print(idx)

    if arr[idx] > key:
      print(-1)

  else : print(-1) # key값이 arr 안의 요소보다 크다면, 탐색 후에도 -1을 리턴하는 절차가 필요 
```