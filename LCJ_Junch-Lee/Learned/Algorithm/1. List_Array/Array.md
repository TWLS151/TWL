## 배열

일정한 자료형의 변수들을 하나의 이름으로 열거하여 사용하는 자료구조 


### 배열의 필요성

- 프로그램 내에서 여러 개의 변수가 필요할 때

  - 배열을 사용하면 하나의 선언을 통해 둘 이상의 변수 선언 

- 단순히 다수의 변수 선언을 의미하는 것이 아님 ! 
  - 다수의 변수로는 하기 힘든 작업(가변, 합) 등을 쉽게 가능하게끔 함


### 1차원 배열

- 1차원 배열에 index를 붙일 경우, 변수로 활용

![1차원 배열 예시](./Array_001.png)

#### 입력받은 정수를 1차원 배열에 저장하는 방법

```python
# 입력 예시
6
2 7 5 3 1 4

N = int(input())
arr = list(map(int, input().split()))
```

### 배열 원소의 합 s 계산하기

```python
s = 0
arr = [2, 7, 5, 3, 1, 4]

for i in range(N): # for i in range(len(arr))
  sum += arr[i]
```

### 배열 원소 중 최댓값 max_value

```python
max_v = arr[0]

for i in range(N):


  if arr[i] > max_v:
    max_v = arr[i]

# 코드의 가독성 높이기
# 조건식에서 연산 순서를 맞춰주기 

  if max_v < arr[i]:
    max_v = arr[i]
```


### 배열의 최댓값의 인덱스 찾기

```python

max_index = 0 # 의미 : 첫 번째 인덱스를 초기값으로

for i in range(N):
  if arr[max_index] < arr[i]:
    max_index = i

# 만약 최댓값이 여러개인 경우?
# 가장 왼쪽의 최댓값의 인덱스가 저장
# 같은 경우에도 무시하기 때문
```

### 찾는 값이 배열에 있으면 해당 원소의 인덱스, 없으면 -1 넣기

- 중요 : 초기값 설정만 잘 해도 추가적인 코드를 많이 줄일 수 있다


```python

# 중요 : 초기 설정을 '없다'고  가정하고 시작 

index = -1

for i in range(N):
  if arr[i] == V:
    index = i
    break # for i : 돌아가는 반복문을 주석으로 표기하자
```


## 연습 문제

### 연습 문제 1

N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하세요.

- 첫 줄에 테스트 케이스 T가 주어진다
- 각 케이스의 첫 줄에 양수의 개수 N이 주어진다.
- 다음 줄에 N개의 양수가 들어있다. 

```python

T = int(input())

arr = list(map(int,input().split()))

for T in range(1, T+1):

  result = 0
  min = 0
  max = 0

  for i in range(len(arr)):

    if min > arr[i]:
      min = arr[i]

    if max < arr[i]:
      max = arr[i]
    
  result = max - min

  print(f"#{T} : {result}")
```
