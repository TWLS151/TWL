# 백트래킹 (Backtracking) 에서의 리팩토링 및 매개변수 설계의 중요성

### 간단. 개념

> `Backtracking`이란, 한 마디로 `똑똑한 탐색`이다. 
> 볼 필요가 없는 경우를 과감히 건너뛰며 최적해를 찾겠다는 접근!

#### 이번 TIL에서는, 간단한 `Powerset` 예제를 통해 백트래킹을 처음 구현해보며 겪은 totally 날것의 공부 과정을 담았다.

---

우선, 부끄럽지만 `S = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`인 집합에서 합이 10이 되는 `Powerset(멱집합)` 찾기를 구현한 본인의 최초 코드를 보자. 

```python
# 입력 데이터를 넣어 재귀를 호출하는 함수

def find_subsets(nums):

    result = []

    backtracking(nums, [], result)

    return result
```

```python
# 실제 재귀 함수

def backtracking(left, current, result):
    
    # 1. 기저 조건 : 해를 찾았는지(완성 여부 판단)
    if sum(current) == 10:
        result.append(list(current)) '''problem 1'''
        return

    # 2. 유망성 판단 (pruning)
    # 이미 합이 10을 넘었다면? 그 경로는 더이상 탐색 X 
    if sum(current) > 10: '''refactoring 1'''
        return

    # 3. 다음 선택지 탐색 (실제 재귀 로직)

    for i in range(len(left)):      

        elem = left[i]          # (1) current에 포함할 원소 선택
        next_arr = left[i+1:]   # 선택으로 인한 상태변화
        current.append(elem)    '''refactoring 2'''

        backtracking(next_arr, current, result)  # (2) 다음 탐색

        current.pop()           # (3) 선택 취소 -> 다음 인덱스를 위해 current 초기화

    return result
```

자, 그럼 하나씩 해체분석을 해보자.


## 1. 최초 코드에서 문제가 되었던 점 (`Probelm 1`)

- `result.append(current)`의 문제

```python
result.append(current)
```

#### 이 코드는 `current` 리스트의 값을 복사한 것이 아니라, 같은 객체의 주소를 저장한 것이다. (이런 기본적인 실수를....)

즉,

- `current`는 재귀 과정에서 계속 수정됨
- `result`에 들어간 모든 원소는 같은 리스트 객체를 참조
- 결국 마지막 상태(ex. `[]`)로 전부 바뀌어버림 !

(심지어 얕은 복사도 아니다... 그냥 참조를 저장한 것)

### 해결 방법

```python
#1
result.append(current[:])

#2
result.append(list(current))

#3
result.append(current.copy())
```

이렇게 설정해야 **그 시점의 스냅샷**이 저장된다. 매우 기본이지만 실수할 경우 디버깅에 오랜 시간을 쏟을 수 있으니. 주의!!!

&nbsp;

## 2. `Backtracking` 세부 로직 피드백

### (1) 문제에 최적화된 코드를 구현했는가? 

A) NO.

- 나의 접근 : 각 상태 공간 트리(경우의 수) 마다 `next_arr` 배열을 새롭게 생성

```python
backtracking(next_arr, ...) # 매번 매개변수로 새로운 배열을 입력한다
```

### 기존 방식의 단점?

- 불필요한 메모리 사용 증가
- 객체 생성 비용 증가
- 시간 + 공간 복잡도 모두 악화시키는 방향

&nbsp;

### 개선 방향 : 모든 재귀마다 하나의 배열을 공유해도 괜찮다

```python
def backtracking(idx, ...)
    # ...

current.append(nums(idx))
backtracking(idx + 1)
current.pop()
```

### 개선 방식의 장점

- 상태 공간 트리 구조는 재귀를 그대로 따르면서
- 데이터 구조는 매우 단순화! 
  - 새로운 배열 -> 인덱스(깊이)

#### 알고리즘 문제 풀이에 있어 사고의 단순화는 필수다

&nbsp;

## (2) 복잡도 or 계산량을 줄이는 매개변수 설정 (연산 횟수 관점에서)

### 핵심 질문. 매번 `sum(current)`를 계산해줘야 할까?

```python
# 1. 기저 조건 및 2. 유망성 판단 로직

if sum(current) == 10: 
  result.append(list(current))
  return

if sum(current) > 10:
  return
```

### 기존 방식의 문제점?

- `sum()`은 `O(N)`
  - 즉, 재귀가 깊어질수록 반복 계산의 포화가 일어남

- 전체 탐색에서 매우 많은 중복 계산

&nbsp;

### 개선 방향 : `current_sum`을 매개변수로 전달하자

```python
def backtracking(idx, current_sum):
```

선택 시, 재귀에서의 활용은

```python
backtracking(idx + 1, current_sum + nums[idx]) # 다음 인덱스, 현재 총합


if current_sum == 10:
  result.append(list(current))
  return 
```

### 개선 방식의 장점

- `sum()` 계산 제거
- 매 단계 `O(1)` 연산
- 기저 조건 검사 단순화
- 불필요한 반복 계산 제거


## 3. 리팩토링 방향성

### 남은 값 중심 -> 위치 중심 사고

기존 : 남은 원소는 뭐지? 

리팩토링 : 현재 나는 몇 번째 인덱스에 있지? 

-> 상태 공간 트리의 레벨을 인덱스로 표현


### 위와 같은 패턴은 중복 탐색 방지 + 조합/부분집합/순열 패턴에 일반화가 가능하다! (꼭 숙지하자)


## 4. 백트래킹을 공부하며 깨달은 것들 


### 가지치기의 본질

: 단순한 '조건 추가'가 아닌, **이 경로는 답이 될 수 없음**을 명확히 지정하는 것

---
### Backtracking의 본질

1. 상태 공간 트리 구성
2. `DFS`로 탐색
3. 최적해 미충족 가지 제거 (`pruning`)
4. (중요) 원상 복구(ex. `.pop()`)

---
### 매개변수 설계가 곧 탐색 설계다

어떤 매개변수를 넘길 것인가
== **내가 이 탐색을 어떻게 이해하고 있는가**

- `idx` : 트리의 깊이
- `current_sum` : 누적 상태
- `current` : 선택 경로

이 세 가지만 잘 설계하면, `Backtracking`은 곧 같은 틀에서의 반복이 된다


## 전체 교훈

> `Backtracking`에서 '가지치기 조건'에만 매몰되지 말자 !
> 성능 차이는 **매개변수 설계와 상태 표현 방식에서 먼저 발생한다.**