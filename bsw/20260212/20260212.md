# 백트래킹
- 후보해를 구성해 나가다가 더 이상 해가 될수 없다고 판단되면 되돌아가서 다른 후보를 찾는 방법
- backtracking과 DFS : DFS는 그래프의 모든 노드에 대한 탐색, backtracking은 완전 탐색 문제에 대한 접근 방법
- pruning(가지치기) : 부분 후보 해가 가능성이 없다면 경로를 따라가지 않고 중지함.

- 진행 절차 : 
1. 상태 공간 트리의 DFS
2. 각 노드의 유망성 점검
3. 유망하지 않으면 부모 노드로 돌아감
4. 검색 지속
---
### 백트래킹으로 미로 찾기?
- DFS 이용 : 무한 루프 x
- 미로 찾기에서 최단 거리를 갔을 때, 더 먼 거리가 걸리는 곳에서 최단 거리와 같은 곳에 다다르면 더 이상 세볼 필요가 없음.
- 알고리즘? 경로 진행을 push하면서 더 이상 진행하지 못하면 stack에서 pop을 진행하면서 경로가 있을 때까지 pop을 진행!
- 아니면 갈 수 있는 경로를 모두 스택에 담아놓고 못 간다고 하면 다른 경로를 사용(기존 경로는 중지)
-  N-Queen 문제 : 모든 경우를 가보면서 확인 or 행과 열의 차이의 절댓값을 이용


### 백트래킹과 부분집합
- 반복문으로 결정하는 방법
```python
bit = [0, 0, 0]
for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[i] = j
        for k in range(2):
            bit [2] = k
            print_subset_(bit)

```
- powerset을 구하는 backtracking 알고리즘
```python
def backtrack(a, k, n):  # a 주어진 배열, k 결정할 원소, n 원소 개수
    c = [0] * MAXCANDIDATES

    if k == n: # 원소의 합이 어떤 수가 되는지 확인 작업(ex: 3이 되는지?)
        process_solution(a, k)  # 답이면 원하는 작업을 한다
    else:
        ncandidates = construct_candidates(a, k, n, c) # c는 진위 판별 여부
        # 후보 개수, 유망한 후보 선택
        for i in range(ncandidates): # 순서대로 꺼냄
            a[k] = c[i] # 값을 결정
            backtrack(a, k + 1, n) # 다음 단계로 가도록 하자
            # 다시 함수로 돌아오는 데 k + 1로 변환

def construct_candidates(a, k, n, c):  # 후보 추천
    c[0] = True  # 원소의 포함 여부
    c[1] = False
    return 2


def process_solution(a, k):
    for i in range(k):
        if a[i]:
            print(num[i], end=' ')
    print()


MAXCANDIDATES = 2
NMAX = 3
a = [0] * NMAX
num = [1, 2, 3]
backtrack(a, 0, 3)
```

# 순열
- 단순하게 생성하는 방법
``` python
for i1 in range(1, 4):
    for i2 in range(1, 4):
        if i2 != i1 :
            for i3 in range(1, 4):
                if i3 != i1 and i3 != i2:
                    print(i1, i2, i3)
```
- backtracking과 순열
```python
def backtrack(a, k, n):
    c = [0] * MAXCANDIDATES

    if k == n:
        for i in range(0, k):
            print(a[i], end=" ")
        print()
    else:
        ncandidates = construct_candidates(a, k, n, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k + 1, n)

def construct_candidates(a, k, n, c):
    in_perm = [False] * (NMAX + 1)

    for i in range(k): # 1이 사용된 적이 있니? 묻는 함수
        in_perm[a[i]] = True

    ncandidates = 0
    for i in range(1, NMAX + 1):
        if in_perm[i] == False:
            c[ncandidates] = i
            ncandidates += 1
    return ncandidates

MAXCANDIDATES = 3
NMAX = 3
a = [0]*NMAX
backtrack(a, 0, 3)
```
- 먼저 1, 2, 3 다 사용이 가능하므로 1부터 진행
- 1을 사용했으므로 2와 3 중에 하나를 선택하는 경우 진행
- 2를 썼으면 3밖에 없으니 3을 넣고 다시 전으로 돌아가서 2를 썻으니 3을 사용 -> 나머지 2를 사용
- 다 사용했으면 맨 위로 돌아가서 2를 사용(반복)
  

  # 가지치기
  - A[i] 원소를 부분집합의 원소로 고려하는 재귀 함수
  ```python
  f(i, N, s, t)
    if s == t
    ...
    elif i == N
    ...
    elif s > t
    ...
    else
        bit[i] = 1
        f(i+1, N, s + A[i], t) # i원소가 포함된 경우
        bit[i] = 0
        f(i+1, N, s, t) # 미포함된 경우
    ```
---

    ```python


    def f(i, k, s, t):  # i원소, k 집합의 크기, s i-1까지 고려된 합, t목표
        global cnt
        global fcnt
        fcnt += 1
        if s > t:   # 고려한 원소의 합이 찾는 합보다 큰경우
            return
        elif s == t:    # 남은 원소를 고려할 필요가 없는 경우
            cnt += 1
            return
        elif i == k:    # 모든원소 고려
            return
        else:
            bit[i] = 1
            f(i+1, k, s+A[i], t)    # A[i] 포함
            bit[i] = 0
            f(i+1, k, s, t)         # A[i] 미포함

    #A = [1,2,3,4,5,6,7,8,9,10]
    N = 10
    A = [ i for i in range(1, N+1)]

    key = 55
    cnt = 0
    bit = [0]*N
    fcnt = 0
    f(0,N,0,key)
    print(cnt, fcnt)      # 합이 key인 부분집합의 수
    ```


# 자리 교환으로 순열 생성하기
- 