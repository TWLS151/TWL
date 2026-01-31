
## 1. 함수(Function)

```python

function_name(arguments) # 함수 이름(arg) 형태

```

- 특정 작업을 수행하기 위한 재사용 가능한 코드 묶음 
- 입력에 대해 정해진 작업을 수행
- 재사용성이 높아지고, 가독성 및 유지보수성 향상 

- 정의 --> 호출 

- 구조
  - Docstring : 설명서
    - 작성한 내용은 이후 호출 시 설명으로 첨부됨
  - function body : 핵심 기능
  - return : 반환 (output), 함수의 결과 
    - 함수의 종료를 의미하기도 함.
    - return 아래에 작성한 코드는 의미 X
    - return 이 없는 경우, 파이썬은 자동으로 `return None`을 추가


### print()는 반환 값이 없다.

### 즉, 반환과 출력은 다르다. 

```python 

def my_func():
    """
    이 함수는 호출되면 터미널에 hello를 출력하는 함수입니다.
    """

    print("Hello!")
    return

my_func() 
# Hello!

result = my_func()
print(result) 
# None.
```

## 2. 매개변수와 인자

- 매개변수(parameter) : 함수 정의 시, 함수가 받을 변수
- 인자(argument) : 함수 호출 시, 실제 전달되는 값 

```python


```

### 다양한 인자 종류

#### (1) 위치 인자 (Positional Arguments)

- 함수 호출 시 인자의 위치에 따라 전달되는 인자
- 위치 인자를 전달하지 않을 시 `TypeError : missing input` 발생
- 가장 먼저 전달해야 함(키워드 인자 뒤에 올 수 없음)

#### (2) 기본 인자 값 (Default Argument Values)

- **함수 정의 시** '매개변수 기본 값'을 설정
- 인자 전달 X시, 함수는 기본 인자를 활용 

#### (3) 키워드 인자 (Keyword Arguments)

- 함수 호출 시 인자의 이름과 함께 값을 전달 
- 인자의 순서가 중요치 않을 때 활용
- 키워드 인자는 **반드시 위치 인자 뒤에 배치**
  
#### 순서의 모호성.

- 컴퓨터는 입력받은 순서대로 작업을 수행하는 '순서 의존' 형태
- 키워드 인자는 순서를 무시하는 지정 형식
- 따라서 컴퓨터는 키워드 인자 이후에 따라오는 값을 인식하지 못해 오류가 발생

#### (4) Arbitrary Argument List (임의의 인자 목록)

- 정해지지 않은 개수의 인자를 처리
- 함수 정의 시 매개변수 앞에 `*` 붙여 사용
- 여러 개의 인자를 tuple로 처리
    - 따라서 추후 사용시 이를 풀어 사용할 필요가 있음

#### (5) Arbitrary Arguments List (임의의 키워드 인자 목록)

- 정해지지 않은 개수의 키워드 인자 처리
- 함수 정의 시 매개변수 앞에 `**` 붙여 사용
- 여러 개의 인자를 dict로 묶어 처리


#### 함수 인자 권장 작성 순서

위치 -> 기본 -> 가변 -> 가변 키워드 


## 3. 재귀 함수 (Recursion fun)

함수 내부에서 자기 자신을 호출하는 함수 

- ex. 팩토리얼 

```python
def factorial(n):
    # 종료 조건 : 0일 경우 1 반환

    if n == 0:
        return 1
    
    else:
        return n * factorial(n-1)

print(factorial(5)) # 120
```

- 반드시 `**base case(종료 조건)**`이 존재해야 하고, 반복되는 호출이 종료 조건으로 수렴하도록 작성해야 함 --> 스택 오버플로우 방지 (Stack overflow)

- 특정 알고리즘 식을 표현할 때 변수 사용이 줄어들며, 가독성이 높아짐


## 4. 내장 함수 (Bulit-in function)

- 파이썬에 기본적으로 저장되어 있으므로, 별도의 패키지 설치 or import 없이 사용이 가능
- ex. `print(), list(), len(), max()`

- cf. 파이썬 공식문서의 내장함수 : `print()`

```python
print(*objects, sep=' ', end='\n', file=None, flush=False)
```

> Print objects to the text stream file, separated by sep and followed by end. sep, end, file, and flush, if present, must be given as keyword arguments.
>
> 모든 비 키워드 인자는 str() 이 하듯이 문자열로 변환된 후 스트림에 쓰이는데, sep 로 구분되고 end 를 뒤에 붙입니다. sep 과 end 는 모두 문자열이어야 합니다; None 일 수도 있는데, 기본값을 사용한다는 뜻입니다. objects 가 주어지지 않으면 print() 는 end 만 씁니다.
>
>file 인자는 write(string) 메서드를 가진 객체여야 합니다; 존재하지 않거나 None 이면, sys.stdout 이 사용됩니다. 인쇄된 인자는 텍스트 문자열로 변환되기 때문에, print() 는 바이너리 모드 파일 객체와 함께 사용할 수 없습니다. 이를 위해서는. 대신 file.write(...) 를 사용합니다.


#### 주의! 

공식 문서의 모든 것을 이해하려고 할 필요 없음. 내가 배운 것들에 집중해서 필요한 것들을 취사선택하면 된다.

my. 오늘 배운 함수의 매개변수에 대해 보면, `print()`는 여러 임의의 인자를 받을 수 있고, `sep = ' '`과 `end = \n` 등으로 구분 및 종료 형식을 지정해줄 수 있다.


## 5. 함수와 Scope

- python의 범위 : 함수는 코드 안에 local scope를 생성하고, 그 외 공간인 global scope로 구분

- scope와 변수의 수명 주기
  - bulit-in scope : 파이썬 실행 이후부터 영원히 
  - global scope : 코드 어디에서든 참조할 수 있는 공간, 모듈 시작 이후 or 인터프리터 끝날 때 까지
  - local scope : 함수가 만든 scope (**함수 내부에서만 참조 가능**) // 함수 호출 시 생성, 함수 종료까지 유지


### 이름 검색 규칙 : LEGB Rule

- Local -> Enclosed -> Global -> Built-in

- 내부 -> 외부로의 찾기는 가능하나, 역으로는 진행되지 않음


### global 키워드

- 변수의 scope를 전역으로 지정하기 위해 사용 
- 전역 변수 수정에 필요

#### 주의사항

- global 키워드 선언 전에 참조 불가
- 매개변수(parameter)에는 global 사용 불가


## 번외. 함수 스타일 가이드

기본 규칙
- 소문자 + 언더스코어`(_)` 
- 동사로 시작, 함수 설명 
- 약어 사용 지양 X, 길어지더라도 정확히 작성

```python

# good

def calculate_total_price

# get/set 접두사 

get_username()

# True, False 반환 

is_~~ () has_ ()

```

- 이름만으로 '무엇을 하는지'를 명확히 표현

### 단일 책임 원칙 :

- 모든 객체는 하나의 명확한 목적과 책임만을 가져야 함

## 함수 설계 원칙 : 한 함수가 하나의 일만 수행하는가

1. 명확한 목적 : 함수는 한 가지 작업만 수행
2. 책임 분리 : 데이터 검증, 처리, 저장 등을 별도 함수로 분리
3. 유지보수성 : 작은 단위의 함수로 나누어 관리

## 패킹(Packing)과 언패킹

: 여러 개의 데이터를 하나의 컬렉션으로 모아 담는 과정 

- `*`를 활용한 패킹 :

    - `*`를 붙인 매개변수가 남는 위치 인자들을 모두 모아 하나의 튜플로 만듦

- `*`를 활용한 언패킹

 - 리스트, 튜플 앞에 `*`를 붙여 개별 위치 인자로 전달 가능

```python

def my_func(*args):
    print(args) # (1, 2, 3, 4, 5)
    print(type(args)) # <class 'tuple'>

my_func(1, 2, 3, 4, 5)

```

- `**`를 활용한 패킹 :

- `**`를 활용한 언패킹

    - 딕셔너리에 `**`를 붙여 {키 : 값} 쌍을 키 = 값 형태의 키워드 인자로 전달 
    - 파라미터와 dict의 키가 일치해야 함

```python

def my_func2(**kwargs):

    print(kwargs) # {'a' : 1, 'b' : 2, 'c' : 3}
    print(type(kwargs)) # <class 'dict'>

my_func2(a = 1, b =2, c = 3)

```

