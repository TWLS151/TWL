## **Python-Fucntion**

**함수(Function)**  
특정 작업을 수행하기 위한 재사용 가능한 코드 묶음  
재사용성, 가독성, 유지보수성 up!  
함수 호출 ```function_name(arguments)```
호출 부분에서 전달된 인자(arguments)는 함수 정의 시 작성한 매개변수에 대입됨  

**함수와 반환값**  
print() 함수는 반환값(return)이 없다. None 반환.  

**매개변수(parameter)**  
함수 정의 시, 함수가 받을 값을 나타내는 변수  

**인자(argument)**  
함수를 호출할 때, 실제로 전달되는 값  
1. 위치 인자
2. 기본 인자
3. 키워드 인자  
호출 시 키워드 인자는 위치 인자 뒤에 위치해야 함!  
1. 임의의 인자 목록 *args  
여러 개의 인자를 tuple로 처리  
1. 임의의 키워드 인자 목록 **kwargs  
여러 개의 인자를 dict로 묶어 처리  

<br>

**재귀함수(recursion)**  
함수 내부에서 자기 자신을 호출하는 함수  
팩토리얼  
종료 조건 필수  
Tree구조나 복잡한 알고리즘(퀵 정렬 등) 구현 시 가독성 good  
```python
def factorial(n):
    # 종료 조건: n이 0이면 1을 반환
    if n == 0:
        return 1
    else:
        # 재귀 호출: n과 n-1의 팩토리얼을 곱한 결과를 반환
        # 재귀 함수는 실행 시, 메모리의 Stack 이라는 공간에 차곡차곡 쌓인다. 
        return n * factorial(n - 1)

# 팩토리얼 계산 예시
print(factorial(5))  # 120
```

<br>


**내장 함수(Bulit-in)**  
import 없이 쓸 수 있는 기본 내장 함수  
```python
numbers = [1, 2, 3, 4, 5]

print(numbers)  # [1, 2, 3, 4, 5]
print(len(numbers))  # 5
print(max(numbers))  # 5
print(min(numbers))  # 1
print(sum(numbers))  # 15
print(sorted(numbers, reverse=True))  # [5, 4, 3, 2, 1]

```  
<br>

**함수와 Scope**  
- Python의 범위(Scope)를 생성하며, 그 외의 공간인 global scope로 구분
- 변수 수명주기  
    1. built-in Scope : 파이썬 실행 이후 끝까지 유지
    2. global scope : 모듈 호출 이후 or 인터프리터 끝까지 유지
    3. local scope : 함수 호출 시 생성, 종료까지 유지
- 이름 검색 규칙 : LEGB rule  

```python
# LEGB Rule 퀴즈
x = 'G'
y = 'G'


def outer_func():
    x = 'E'
    y = 'E'

    def inner_func(y):
        z = 'L'
        print(x, y, z)  # E P L

    inner_func('P')
    print(x, y)  # E E


outer_func()
print(x, y)  # G G

```
<br>

**전역 변수**  
- 변수의 스코프를 전역 범위로 지정하기 위해 사용  
- 장점 : 여러 함수나 모듈에서 공통으로 참조해야 하는 설정값 관리 용이, 함수 매개변수 최소화 등  
- 단점 : 규모 큰 프로젝트 경우 문제, 암묵적 결합(추적 어려움), 메모리 낭비, 전역 공간은 하나라 이름이 겹치면 기존 변수 덮어버리는 참사...등  

```python
num = 0  # 전역 변수

def increment():
    global num  # num를 전역 변수로 선언
    num += 1

print(num)  # 0
increment()
print(num)  # 1

# ‘global’ 키워드 주의사항 1 - global 키워드 선언 전에는 참조불가
num = 0

def increment():
    # SyntaxError: name 'num' is used prior to global declaration
    print(num)
    global num
    num += 1

# ‘global’ 키워드 주의사항 2 - 매개변수에는 global 키워드 사용불가
num = 0

def increment(num):
    # SyntaxError: name 'num' is parameter and global
    global num
    num += 1
```
```python
# 누적 카운트 시에 전역 변수 사용 예시
# 전역 변수 (공유 상태)
total_visitors = 0

def visit_page(user_name):
    global total_visitors  # 함수 내에서 전역 변수를 수정하겠다고 선언
    total_visitors += 1
    print(f"{user_name}님이 방문했습니다. (총 방문자: {total_visitors})")

def show_statistics():
    print(f"오늘의 총 방문자 수는 {total_visitors}명입니다.")

visit_page("Alice")
visit_page("Bob")
show_statistics()
```

<br>

**Packing&Unpacking**  

- **Packing** : 여러 개의 데이터를 하나의 컬렉션(튜플)으로 모아 담는 과정  
```python
packed_values = 1, 2, 3, 4, 5
print(packed_values)  # (1, 2, 3, 4, 5)

# ‘*’ 을 활용한 패킹 (함수 매개변수 작성 시)
def my_func(*args):
    print(args)  # (1, 2, 3, 4, 5)
    print(type(args))  # <class 'tuple'>

my_func(1, 2, 3, 4, 5)

# ‘**’ 을 활용한 패킹 (함수 매개변수 작성 시)
def my_func2(**kwargs):
    print(kwargs)  # {'a': 1, 'b': 2, 'c': 3}
    print(type(kwargs))  # <class 'dict’>

my_func2(a=1, b=2, c=3)
```  

- **Unpacking** : 컬렉션에 담겨있는 데이터들을 개별 요소로 펼쳐 놓는 과정  
시퀀스 언패킹 또는 다중 할당이라고 부름  
```python
packed_values = 1, 2, 3, 4, 5

# 언패킹
a, b, c, d, e = packed_values
print(a, b, c, d, e)  # 1 2 3 4 5

# ‘*’ 을 활용한 언패킹 (함수 인자 전달)
def my_function(x, y, z):
    print(x, y, z)

names = ['alice', 'jane', 'peter']
my_function(*names)  # alice jane peter

# ‘**’을 활용한 언패킹 (딕셔너리 -> 함수 키워드 인자)
def my_function(x, y, z):
    print(x, y, z)

my_dict = {'x': 1, 'y': 2, 'z': 3}
my_function(**my_dict)  # 1 2 3
```

<br>


**Lamda 표현식**  
- 한 줄로 간단한 함수를 정의, 함수 이름은 익명  
```python
# 람다 표현식 적용 전
def addition(x, y):
    return x + y

# 람다 표현식 적용 후
lambda x, y: x + y

"""
람다 표현식 활용 (with sorted 함수)
sorted() 함수는 리스트를 정렬해주며, key라는 매개변수에 함수를 전달하여 
"무엇을 기준으로 정렬할지"를 지정할 수 있습니다. 
이때 간단한 기준을 제시하기 위해 lambda를 사용하는 것이 매우 효과적입니다.

예시: 학생들의 점수를 나이순으로 정렬하기
학생 데이터가 (이름, 나이) 형태의 튜플로 묶여있는 리스트가 있다고 가정해 봅시다

# 목표: 학생들을 '나이'가 어린 순서대로 정렬하고 싶다!
"""
# 학생 데이터가 (이름, 나이) 형태의 튜플로 묶여있는 리스트
students = [('지민', 25), ('서준', 20), ('민우', 30)]

# 1. lambda 미사용
# 정렬 기준 함수를 굳이 정의해야 함
# student
def get_age(student):
    return student[1]

# sorted 함수의 key 매개변수에 우리가 만든 get_age 함수를 전달
result = sorted(students, key=get_age)
print(result)  # [('서준', 20), ('지민', 25), ('민우', 30)]

# 2. lambda 사용
"""
get_age처럼 간단하고 한 번만 쓸 함수를 굳이 따로 정의할 필요 없이, lambda로 즉석에서 만들어 전달할 수 있습니다.
key=lambda student: student[1]
-> "정렬할 때 각 데이터를 student라고 부를게."
-> "그리고 그 데이터의 1번 인덱스 값(나이)을 기준으로 삼아줘."
"""
result = sorted(students, key=lambda student: student[1]) # student는 임시 상자...
print(result)  # [('서준', 20), ('지민', 25), ('민우', 30)]
```
<br>


### **재귀 함수 활용 예시**  
- 복잡하게 꼬인 리스트 평탄화
```python
# 복잡하게 꼬인 리스트 평탄화
# 약 리스트가 [1, [2, [3, 4], 5], 6]처럼 무작위로 겹쳐있을 때, 모든 숫자를 꺼내서 하나의 일렬 리스트로 만들고 싶다면 재귀가 가장 깔끔한 정답!

# 함수 정의 data 받아 처리
def flatten(data):
    # 빈 리스트 준비
    result = []
    # data에서 재료 꺼내 보기 반복문
    for item in data:
        if isinstance(item, list):  # 만약 리스트라면?
            result.extend(flatten(item))  # 재귀! 리스트 안에 리스트가 있다는 뜻이므로, 다시 flatten 함수를 불러서 안으로 들어감
        else:
            result.append(item)  # 리스트가 아니라면? 결과 리스트에 담음
    return result

nested_list = [1, [2, [3, 4], 5], 6]
print(flatten(nested_list))  # [1, 2, 3, 4, 5, 6]
```

- 10진수 → 2진수 변환 재귀함수
  
```python
def decimal_to_binary(n):
    # 1. 기저 조건 (Base Case): 재귀를 멈추는 지점
    if n == 0:
        return ""
    
    # 2. 재귀 호출과 나머지 연산
    # n을 2로 나눈 몫을 다시 함수에 넣고, 나머지를 문자열로 더함
    return decimal_to_binary(n // 2) + str(n % 2)

# 테스트
num = 13
print(f"{num}의 2진수: {decimal_to_binary(num)}")
# 출력 결과: 1101
```