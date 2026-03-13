### 260309
<br>

> **이차원리스트의 합**
```python
board = [[1, 2], [3, 4]]
print(sum(board))
# TypeError: unsupported operand type(s) for +: 'int' and 'list'
```
- 혹시 될까 해서 해봤는데 역시 안된다...

```python
print(sum(sum(x) for x in board))  # 10
```
- 귀찮지만 이게 정석

<br>
<br>

> **최댓값 여러 개 추출**

```python
import heapq
data = [3, 5, 2, 8]
print(heapq.nlargest(2, data))
```
<br>
<br>

---
### 260310
<br>

> **global 선언**

```python
def test_1(x):
    x += 1
    print(f'테스트1 함수 안 x: {x}')  # 4

x = 3
test_1(x)  # 4
print(f'테스트1 함수 밖 x: {x}')  # 3 >> 변화 없음
```
- 매개변수로 전달된 x는 '지역 변수'
- 함수 밖 x의 '값'만 복사해왔으므로, 함수 내에서 변경해도 외부 x에는 영향이 없음

<br>

```python
def test_2():
    global x
    x += 1
    print(f'테스트2 함수 안 x: {x}')  # 4

x = 3
test_2()   # 4
print(f'테스트2 함수 밖 x: {x}')  # 4 >> 전역 변수 변경
```
- global 선언: 함수 밖의 전역 변수 x를 직접 참조
- 함수 안에서의 변경이 실제 전역 변수 x의 값을 바꿈

<br>

```python
def test_3():
    y[1] = 2
    print(f'테스트3 함수 안 y: {y}')  # [0, 2]

y = [0, 1]
test_3()  # [0, 2]
print(f'테스트3 함수 밖 y: {y}')  # [0, 2] >> 내부 요소 변경
```
- 전역 변수 y(리스트)의 '내부 요소' 수정
- 리스트는 가변 객체이므로 global 선언 없이도 참조 및 내부 수정이 가능

<br>

```python
def test_4():
    y = [2, 3]
    print(f'테스트4 함수 안 y: {y}')  # [2, 3]

y = [0, 1]
test_4()  # [2, 3]
print(f'테스트4 함수 밖 y: {y}')  # [0, 2] >> 외부 변수 변화 없음
```
- y라는 이름에 '새로운 리스트'를 할당
- 이 순간 y는 전역 변수가 아닌 이 함수만의 '지역 변수'로 새로 정의됨
- 따라서 함수 밖의 y에는 아무런 영향을 주지 않음

<br>

```python
def test_5():
    global y
    y = [4, 5]
    print(f'테스트5 함수 안 y: {y}')  # [4, 5]

y = [0, 1]
test_5()  # [4, 5]
print(f'테스트5 함수 밖 y: {y}')  # [4, 5] >> 전역 변수 재할당
```
- global 선언: 전역 변수 y 자체를 새로운 리스트로 교체

<br>
<br>

> **[주의] in**
```python
if i in path:
    pass
```
- 시간복잡도: O(N)
- 시간 초과 가능성 증가하므로 사용 지양

<br>
<br>

> **[Tip] 함수 내 조건문**
```python
# 1
if [조건]:
    pass

# 2
if not [조건]:
    continue
```
- 가독성을 위해 1보다 2 지향