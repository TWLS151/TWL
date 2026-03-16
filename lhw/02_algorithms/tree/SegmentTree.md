# SEGMENT TREE


## 목차
- [세그먼트 트리?](#세그먼트-트리)
- [연습문제](#연습문제)
    - [ABC 448 C](#abc-448-c---구간-내-최소값-구하기)
    - [BOJ 2042](#boj-2042---구간-합-구하기)
    - [BOJ 11505](#boj-11505---구간-곱-구하기)
    - [BOJ 2357](#boj-2357---최소-최대값-구하기)
- [알아야 해!](#알아야-해)

---

## 세그먼트 트리?
  
세그먼트 트리는 이름에서 나와있듯 우선 `트리`인데 배열의 연속한 구간에 대해 질의(query)와 갱신(update)를 효율적으로 수행할 수 있도록 설계된 이진 트리 기반 자료구조이다.

누적합의 개념과 비슷하지만 우선 누적합은 합계를 구할 때만 사용할 수 있고 배열 내부의 값이 변경되면 사용할 수 없다는 점이 세그먼트 트리와는 다르다. ( 사용은 가능하겠지만 사실상 처음부터 계산을 다시하는 것으로 비용이 매우 커진다. )
  
트리에 대해 어느정도 알고 있다면 이해하는 데 크게 무리는 없을 것이다.

---

## 연습문제

### ABC 448 C - 구간 내 최소값 구하기

[문제 링크](https://atcoder.jp/contests/abc448/tasks/abc448_c)  
(*일본어로 표시된다면 페이지 우상단에 영어로 전환하는 버튼이 있다.*)

다음은 `At-Coder Begginer Contest 448 - C` 문제의 풀이이다.  
쿼리에서 주어지는 인덱스의 값을 제외하고 배열 내 최소값을 찾는 문제이다.

```python
INF = 10 ** 18

N, Q = map(int, input().split())
A = list(map(int, input().split()))


# --- 세그먼트 트리 크기 결정 및 생성 --- #
size = 1
while size < N:
    size *= 2

seg = [INF] * (2 * size)
# ----------------------------------- #

# --- 트리의 리프노드를 채우는 반복문 --- #
for i in range(N):
    seg[size+1] = A[i]
# ---------------------------------- #

# --- 리프노드의 부모노드부터 루트노드까지 채우는 반복문 --- #
for i in range(size-1, 0, -1):
    seg[i] = min(seg[i*2], seg[i*2 + 1]) 
# -------------------------------------------------- #

# --- 문제에서 요구하는 인덱스의 값을 변경한 뒤 위의 노드까지 갱신 --- #
def update(idx, value):
    node = size + idx
    seg[node] = value
    node //= 2
    while node:
        seg[node] = min(seg[node * 2], seg[node * 2 + 1])
        node //= 2
# ----------------------------------------------------------- #

for _ in range(Q):
    K = int(input())
    B = list(map(int, input().split()))

    removed = []
    for b in B:
        b -= 1
        removed.append(b)
        update(b, INF)
    
    print(seg[1])

    for b in removed:
        update(b, A[b])
```

해당 문제는 해결을 위해 반드시 세그먼트 트리를 채용해야하지는 않지만 `배열의 일부를 수정하고 연산한다.` 라는 방식이기에 세그먼트 트리를 사용하기에 적합하다.  

~~**[1]** 위 코드의 `트리 크기 결정 및 생성`은 다음의 코드로 대체 가능하다.  
`seg = [INF] * (4 * N)`  
세그먼트 트리는 완전 이진 트리가 전제 조건이므로 전체 크기는 2의 제곱의 형태가 되는데 그 값을 정확하게 계산하면 `4N` 보다 조금 작은 수가 나온다.  
최적화를 한다면 위 코드 내의 방식을 사용하는 것이고 그렇게까지는 필요가 없다면 4N을 사용한다.~~  

**대체 불가능**
  
4N 을 채용하는 방식은 `seg`를 진짜 트리로 구현하는 방식이고, 위 코드의 방식은 배열로 구현하는 방식이라 차이가 있다.  

배열로 구현하는 방식은 우선 `seg`를 `포화 이진트리`로 만들고 리프노드에 주어진 배열의 값을 하나 씩 채운 뒤 남는 리프는 `0`으로 채우는 방식이다. ( 곱이라면 `1` )

  
### BOJ 2042 - 구간 합 구하기

[문제 링크](https://www.acmicpc.net/problem/2042)

```python
# BOJ - 2042 - 구간 합 구하기
# 세그먼트 트리 연습 문제

import sys
input = sys.stdin.readline

def update(idx: int, value: int):
    global seg, size

    idx += size
    seg[idx] = value

    # idx 의 부모 노드는 idx//2
    node = idx // 2

    # 이걸 루트노드까지 가야함
    while node > 0:
        seg[node] = seg[2*node] + seg[2*node + 1]
        node //= 2


def query(start: int, end: int):
    global seg

    '''
    size + idx 가 시작해야하는 리프노드가 된다.
    range(size + start, size + end)
    '''
    start += size
    end += size
    result = 0

    while start <= end:
        if start % 2 == 1:
            result += seg[start]
            start += 1
        
        if end % 2 == 0:
            result += seg[end]
            end -= 1
        
        start //= 2
        end //= 2

    return result


N, M, K = map(int, input().split())
nums = [int(input().strip()) for _ in range(N)]

# --- 트리 구현 --- #
size = 1
while size < N:
    size *= 2

seg = [0] * (2 * size)

# 리프노드 채우고
for i in range(N):
    seg[size+i] = nums[i]

# 자식노드의 합으로 부모노드 채우기
for i in range(size-1, 0, -1):
    seg[i] = seg[2*i] + seg[2*i+1]
# ---------------- #
    
for _ in range(M+K):
    order, B, C = map(int, input().split())
    B -= 1

    # pre_val = []  백트래킹 필요 없다.
    if order == 1:
        # pre_val.append((B, nums[B]))
        update(B, C)

    else:
        C -= 1
        print(query(B, C))
```

### BOJ 11505 - 구간 곱 구하기

[문제 링크](https://www.acmicpc.net/problem/11505)

```python
# BOJ - 11505 - 구간 곱 구하기
import sys
input = sys.stdin.readline

'''
구간 합 구하기 문제에서 덧셈을 곱셈으로만 바꿔주면 되는 문제
모든 값에 MOD 연산을 해주어야한다. 안그럼 터진다.
'''
MOD = 1000000007

def update(idx: int, value: int):
    global seg, size

    idx += size
    seg[idx] = value % MOD

    node = idx // 2

    while node > 0:
        seg[node] = (seg[2*node] * seg[2*node + 1]) % MOD
        node //= 2


def query(start: int, end: int):
    global seg

    start += size
    end += size
    result = 1

    while start <= end:
        if start % 2 == 1:
            result = (result * seg[start]) % MOD
            start += 1
        
        if end % 2 == 0:
            result = (result * seg[end]) % MOD
            end -= 1
        
        start //= 2
        end //= 2

    return result


N, M, K = map(int, input().split())
nums = [int(input().strip()) for _ in range(N)]

size = 1
while size < N:
    size *= 2

seg = [1] * (2 * size)

for i in range(N):
    seg[size+i] = nums[i] % MOD

for i in range(size-1, 0, -1):
    seg[i] = (seg[2*i] * seg[2*i+1]) % MOD
    

for _ in range(M+K):
    order, B, C = map(int, input().split())
    B -= 1

    if order == 1:
        update(B, C)

    else:
        C -= 1
        print(query(B, C))
```

### BOJ 2357 - 최소, 최대값 구하기

[문제 링크](https://www.acmicpc.net/problem/2357)

```python
# BOJ - 2357 - MinValue && MaxValue

import sys
input = sys.stdin.readline

def find_val(start: int, end: int, size: int, seg: list) -> int:

    start += size
    end += size

    min_val = seg[start][0]
    max_val = seg[end][1]

    while start <= end:
        if start % 2 == 1:
            min_val = min(min_val, seg[start][0])
            max_val = max(max_val, seg[start][1])
            start += 1
        
        if end % 2 == 0:
            min_val = min(min_val, seg[end][0])
            max_val = max(max_val, seg[end][1])
            end -= 1

        start //= 2
        end //= 2

    return min_val, max_val


N, M = map(int, input().split())
nums = [int(input().strip()) for _ in range(N)]

INF = 10**18

size = 1
while size < N:
    size *= 2

seg = [[INF, 0] for _ in range(2*size)]

for i in range(N):
    seg[size + i][0] = nums[i]
    seg[size + i][1] = nums[i]

for i in range(size-1, 0, -1):
    seg[i][0] = min(seg[i*2][0], seg[i*2+1][0])
    seg[i][1] = max(seg[i*2][1], seg[i*2+1][1])

for _ in range(M):
    start, end = map(int, input().split())
    start -= 1
    end -= 1

    print(*find_val(start, end, size, seg))
```

---

## 알아야 해!

아마 어느정도 이해도가 없다면 무슨 말인지 모를 것이다. 위의 BOJ 문제들을 보다보면 `query` 부분에서 막힐 수도 있는데 그 때 와서 확인하면 도움이 될 것 같다.

**[*] 중요한 관찰 [*]**

각 레벨에서

왼쪽 경계
오른쪽 경계

딱 두 개의 `포인터`만 존재한다.

l ----------- r

이 두 포인터 사이의 노드들은 이미 부모 노드로 합쳐진 상태.  
=> `독립된 노드`만 확인하면 되고 이 `독립 여부`를 판단하는게

l % 2 == 1 ?
r % 2 == 0 ?

l % 2 == 1 이면 l 포인터가 오른쪽 자식이라는 뜻이고 고립되었다는 뜻
r % 2 == 0 이면 r 포인터가 왼쪽 자식이고 고립되었다는 뜻