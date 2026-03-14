
> BOJ - 14888 [연산자 끼워넣기]  

```PYTHON
# BOJ - 14888
# 연산자 끼워넣기

# 1. 상태 정의
'''
연산자의 선택 현황 // 남은 연산자의 갯수
'''
# 2. 선택
'''
남은 연산자 중 하나를 선택한다
'''
# 3. 제약
'''
연산자의 우선순위는 무시하고 앞에서부터 계산한다.
'''
# 4. 백트래킹 ( 필요 시 )
'''
계산이 끝나면 그 계산에서 사용된 연산자 갯수를 다시 되돌린다.
'''

N = int(input())  # 숫자의 갯수
nums = list(map(int, input().split()))  # 연산을 진행해야하니 정수로
# 앞에서부터 계산해야하는데 그럼 뒤집어서 뒤에서부터 계산하는 것도 괜찮겠다.
nums.reverse()

# 순서대로 + - * // [0, 1, 2, 3]
op_lst = list(map(int, input().split())) 

max_val = float('-inf')
min_val = float('inf')



# [0: +, 1: -, 2: *, 3: //] #
def dfs(nums, op_lst):
    global max_val, min_val

    # 기저: 남은 연산자가 없으면 종료
    if len(nums) == 1:
        max_val = max(max_val , nums[0])  # 진입
        min_val = min(min_val , nums[0])  # 진입
        return

    # 반복
    for idx in range(4):
        if op_lst[idx] != 0:  # 연산자가 남아있으면
            op_lst[idx] -= 1  # 하나 사용
            nnums = nums[:]
            if idx == 0:
                adds = nums.pop() + nums.pop()
                nums.append(adds)
            elif idx == 1:
                adds = nums.pop() - nums.pop()
                nums.append(adds)
            elif idx == 2:
                adds = nums.pop() * nums.pop()
                nums.append(adds)
            else:
                adds = int (nums.pop() / nums.pop())
                nums.append(adds)
            
            dfs(nums, op_lst)

            op_lst[idx] += 1  # 계산 끝나면 되돌림
            nums = nnums[:]

dfs(nums, op_lst)

print(max_val)
print(min_val)    
```

힌트를 조금 받긴 했지만 해결 했습니다. 조금 어려웠던 부분은 역시 백트래킹이었습니다.  
연산자 백트래킹은 문제 없이 진행했으나 `nums` 또한 백트래킹 해야한다는 점을 간과했습니다. 그래도 중간에 알아차리고 정상화 했습니다.  
그리고 MAX와 MIN 밸류 값을 갱신하는 위치를 잘 못 잡아서 또 잠깐 헤맸습니다.

AI 피드백 내용은 다음과 같습니다.  
1. `nums`의 백트래킹 방식이 불안하다.  
슬라이싱을 활용한 백트래킹은 nums의 값을 바꾸는 게 아니라 참조하는 주소를 변경하는 거라서 백트래킹이라고 하기 힘들고 구조가 조금만 복잡해져도 바로 터질 수 있다.  
다음과 같이 하는게 최선.
    ```python
    a = nums.pop()
    b = nums.pop()

    # calculation
    nums.append(calculated_val)

    dfs()

    nums.pop()

    nums.append(b)
    nums.append(a)
    ```

2. 나눗셈 방식  
받은 힌트 중 가장 큰 부분인데 나머지는 어떻게 다 구현을 해서 출력이 나오긴 하는데 값이 조금씩 달라 헤멨습니다만 나눗셈의 방법이 문제였습니다. `nums.pop() // nums.pop()` 해서 값을 구했는데 이렇게 하면 음수가 값에 포함되어 있을 때 의도한 값이 나오지 않는 경우가 있습니다.  
`-7 // 2 == -3` 이 되어야하는데 파이썬의 `//` 연산자는 음수에서 `내림`이기에 `-4`가 되어버립니다. 그래서 `//` 연산자가 아닌 `/`을 사용하고 계산 값을 `int`로 감싸는 방식을 취해야한다고 합니다.
----
> 리팩터링 코드
```python
# BOJ 14888 - 리팩터링(스택 방식 유지)

import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
nums.reverse()  # 뒤집어서 pop()이 "앞에서부터"의 왼쪽 피연산자가 되도록 만들기
ops = list(map(int, input().split()))  # +, -, *, //

max_val = -10**18
min_val = 10**18

def apply(op_idx: int, a: int, b: int) -> int:
    if op_idx == 0:
        return a + b
    if op_idx == 1:
        return a - b
    if op_idx == 2:
        return a * b
    # op_idx == 3
    return int(a / b)  # 0을 향해 버림

def dfs():
    global max_val, min_val

    if len(nums) == 1:
        v = nums[0]
        if v > max_val: max_val = v
        if v < min_val: min_val = v
        return

    # 뒤집어놨기 때문에 pop() 두 번이면
    # a = (원래 수열에서) 더 앞에 있던 값
    a = nums.pop()
    b = nums.pop()

    for op_idx in range(4):
        if ops[op_idx] == 0:
            continue

        ops[op_idx] -= 1
        res = apply(op_idx, a, b)
        nums.append(res)

        dfs()

        nums.pop()        # res 제거
        ops[op_idx] += 1  # 연산자 복구

    # 다음 분기를 위해 a,b도 복구
    nums.append(b)
    nums.append(a)

dfs()

print(max_val)
print(min_val)
```

> 정석코드
```python
# BOJ 14888 - 정석(인덱스 + 누적값)

import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))  # +, -, *, //

max_val = -10**18
min_val = 10**18

def dfs(i: int, cur: int):
    global max_val, min_val

    if i == N:
        if cur > max_val: max_val = cur
        if cur < min_val: min_val = cur
        return

    x = nums[i]

    if ops[0] > 0:
        ops[0] -= 1
        dfs(i + 1, cur + x)
        ops[0] += 1

    if ops[1] > 0:
        ops[1] -= 1
        dfs(i + 1, cur - x)
        ops[1] += 1

    if ops[2] > 0:
        ops[2] -= 1
        dfs(i + 1, cur * x)
        ops[2] += 1

    if ops[3] > 0:
        ops[3] -= 1
        dfs(i + 1, int(cur / x))  # 0을 향해 버림
        ops[3] += 1

dfs(1, nums[0])
print(max_val)
print(min_val)
```
제 코드의 함수는 for문을 채용했었는데 정석코드를 보니 불필요한 요소였습니다. 확실히 if문을 활용하는 방식이 더 직관적이기도 하고 원본 리스트를 건드리지 않는다는 점에서 더 좋은 코드인 것 같습니다.

원본을 건드리지 않으려고 해봤었는데 잘 안되어서 결국 그냥 구현했었는데 이 부분을 잘 보고 기억해야겠습니다.