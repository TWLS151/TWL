## **Python - Basic syntax 1** 

**평가** : 표현식을 계산하여 그 결과인 '값'을 만들어내는 과정, 값이 안남으면 표현식이 아니라 문장

**변수** : 값을 나중에 다시 사용하기 위해, 그 값에 붙여주는 고유한 이름 / 특정 객체를 가리키는 이름표

**변수 할당** : 표현식이 만들어 낸 값에 이름을 붙이는 과정

**재할당** : 만약 변수명이 이전에 다른 객체를 가리키고 있었다면, 그 연결은 끊어지고 새로운 객체와의 연결만 남음

**타입** : 변수나 값이 가질 수 있는 데이터의 종류  
타입은 '값'과 '연산자'로 구분한다.

**메모리 주소** : 메모리의 모든 위치에는 그 위치를 고유하게 식별하는 메모리 주소가 존재  

**객체** : 값+타입+메모리 주소 정보를 묶은 것

**Numeric types** : int, float, complex

**Text types** : str  -> **변경 불가능**한 **시퀀스** 자료형

**Squence types** : str, list, tuple, range  
여러 데이터가 순서대로 일렬로 늘어선 자료구조 (정렬이 아님)  
**인덱스** : 값 위치 고유 번호 (0번 부터)  
음수 인덱스도 활용 -> 마지막 값은 [-1]  
```my_sequence[start : stop(포함x) : step(간격)]```  
거꾸로 [::-1]  
슬라이싱  
길이 len() 구하기 가능  
반복문  
    
**Non-sequence types** : set, dict

**기타** : Boolean, None, Function  

<br>

## **Python - Version control1**

CLI : Command Line Interface

Git : 분산 버전 관리 시스템  
Working Directory, Staging Area, Repository  

<br>


## **Python - Basic Syntax2**

**list**
- 여러 개의 값을 1.순서대로 저장하는, 2.변경 가능한(mutable) 시퀀스 자료형
- 중첩 리스트 접근
my_list = [ 1, 'a', 2, [1,2,'3']]
- 인덱싱, 슬라이싱, 길이

```python
my_list = [1, 2, 3, 4, 5]
# 인덱싱으로 값 수정 가능
my_list[1] = 'two' # [1, 'two', 3, 4, 5]
# 슬라이싱으로 여러 값 한번에 바꾸기
my_list[2:4] = ['three', 'four'] # [1, 2, 'three', 'four', 5]
```
<br>

**tuple**
- 여러 개의 값을 1.순서대로 저장하는, 2.변경 불가능한 시퀀스 자료형
- 리스트와 비슷하지만, 한번 만들어지면 절대 수정할 수 없다. 
my_tuple = (1,) *단일 요소 튜플을 만들 때는 반드시 후행 쉼표를 사용해야 한다.
- 인덱싱, 슬라이싱, 길이
- 튜플의 패킹과 언패킹에 대해 이해하기

```python

x, y = 1, 2
# 내부 동작 : (1, 2)라는 튜플을 생성한다. 

x, y = y, x
# 우변을 좌변보다 먼저 처리한다.
# y, x를 먼저 일어 임시 튜플 (2, 1)을 만든다. -> 안전하다! 원래 변수 x, y와는 별개의 독립적인 메모리 공간에 존재하기 때문이다. 나중에 좌변의 x값이 바뀌더라도, 복사된 값은 영향 받지 않고 그대로 유지. 튜플같은 중간 매개체가 없다면, x를 바꾸는 순간 원래의 x값이 사라져 y에게 줄 값이 없어지게 된다.
# 우변 (2, 1)에서 값을 하나씩 꺼내 왼쪽 변수에 다시 할당한다.
# 2 -> x에게 새로부여, 1-> y에게 새로 부여

# 튜플이 수정된 것이 아니며, 변수 x와 y가 가리키는 대상(메모리 주소)이 바뀐 것이다. 
# 왜 안전한가? 오른쪽에서 복사본(튜플)을 미리 만들어두기 때문에, x에 값을 넣는 순간 원래 x값이 사라져도 상관없기 때문이다.
```

<br>

**range**
- 연속된 정수 시퀀스를 생성하는, 2.변경 불가능한 자료형
- 주로 반복문과 함께 사용, 특정 횟수만큼 코드 반복 실행   
```range(Start, stop, step)```   
*매개변수(인자)가 하나면 stop으로 인식한다.   
start는 0, step은 1 기본 설정.  
```range(5) #0,1,2,3,4  ```  
list()로 형변환시 내부 값 확인 가능!

<br>

**dict**
- 키, 값의 쌍으로 이루어진 1.순서와 중복이 없는 2.변경 가능한 자료형  
```my_dict = {'key':'value', 'apple':12}```  
- key는 중복될 수 없음, 변경 불가능한 자료형만 가능.(list,dict은 불가능함. tuple은 가능함.)  
```python
# 값 접근 방법  
my_dict['key'] #'value'
# 값 추가 및 변경
my_dict['new_key'] = 'new_value'
my_dict['key'] = 'value_2'
```

<br>

**set**
- 1.순서와 중복이 없는 2.변경 가능한 자료형
```python
my_set_1 = set()
my_set_2 = {1,2,3}
# 집합 활용 효과적
'''합집합 a|b
차집합 a-b
교집합 a&b '''
```

<br>

**None**  
값이 없음을 표현하는 데이터 타입

**Boolean**  
참과 거짓의 값만 가진 데이터 타입  

**collection**  
- 여러 개의 값을 하나로 묶어 관리하는 자료형을 통칭하는 말  
str, list, tuple, range, set, dict

| 자료형 | 변경 가능 (Mutable) | 순서 존재 (Ordered) | 특징 및 용도 |
| :--- | :---: | :---: | :--- |
| **문자열 (str)** | **X** | **O** | 텍스트 데이터, 튜플처럼 수정 불가능 |
| **리스트 (list)** | **O** | **O** | 가장 범용적인 가변 시퀀스 |
| **튜플 (tuple)** | **X** | **O** | 값의 보호, 값 교환 및 백업용 |
| **세트 (set)** | **O** | **X** | 중복 제거, 집합 연산 |
| **딕셔너리 (dict)** | **O** | **X or O** | 키-값 쌍 저장 (3.7+ 순서 유지) |

---
<br>

**형변환**

**암시적 형변환**  
- 정수와 실수의 연산은 실수형으로, 불리언과 정수의 연산은 정수형으로, 불리언간 연산이 실수형으로...  
- Boolean과 Numeric Type에서만 가능  
(True -> 1, False -> 0)  


**명시적 형변환**  
int(), str(), float()  
```python
list("abc") # ['a', 'b', 'c']
tuple([1,2]) # (1, 2)
set([1,2,2]) # {1,2}
# !! 세트는 중복 불가 !!

int('3.5') # 바로 불가능. float('3.5')이후, 가능.
```

<br>

**산술 연산자**  
 -, +, -, *, /, //, %, **  

**복합 연산자**  
```python
a += b #a=a+b
a -= b #a=a-b
a *= b #a=a*b
a /= b #a=a/b
a //=b #a=a//b
a %= b #a=a%b
a **= b #a=a**b
```
  

**비교 연산자**  
<,>,=,==,!=,is,is not  
==는 동등성 판별, 값이 같은지 비교  
is는 식별성 판별, 두 변수가 완전히 동일한 메모리 주소의 객체를 가리키는지, 즉, 정체성이 같은지를 확인  
is 연산자는 주로 싱글턴 객체를 비교할 때 사용함  
 - singleton 객체란?  특정 값에 대해 파이썬 전체에서 단 하나의 객체만 생성되어 재사용되는 특별한 객체 (e.g. None, True, False)  


**논리 연산자**  
and, or, not  

**단축 평가**  
논리 연산에서 두 번째 피연산자를 평가하지 않고 결과를 결정하는 동작  
비어있거나 없다는 느낌의 값은 False  

**멤버십 연산자**  
in, not in  

**시퀀스형 연산자**  
시퀀스 자료형(문자열, 리스트, 튜플)에 사용  
+은 연결, *은 반복  

<br>

### 슬라이싱 문제 [ws_1_c]

```python
# password 문자열에서 index 번호로 슬라이싱하기
password = "In the bustling city, where life is a constant race against time, uoy often find yourself wondering if there's a shortcut to success. The vibrant lights of the cityscape illuminate the night, casting shadows on the short-lived dreams of those who seek fortune. As you navigate through the crowded streets, you realize the deen for guidance, like a compass pointing python. You need direction in this chaotic journey called life."
# 28번째부터 35번째까지
first_char = password[28:36]
# 113번째부터 총 5글자
second_word = password[113:118]
# 66번째부터 68번째 글자 뒤집어서
third_word = password[66:69][::-1] # 혹은 [68:65:-1] 또한 가능 # 주의 [66:69:-1]는 불가능
# 322번째부터 총 4글자 뒤집어서 
fourth_word = password[322:327][::-1]
# 365번째부터 작성된 'python'
fifth_word = password[365:371]

my_str = f'{first_char}{second_word} {third_word}{fourth_word} "{fifth_word}".'
print(my_str)
# life is short you need "python". 
```
### Escape Sequence - 문자열 안의 특수 기호 활용하기

| 이스케이프 시퀀스 | 기능 | 설명 |
| :--- | :--- | :--- |
| `\n` | 줄바꿈 | 커서를 다음 줄로 이동 (Newline) |
| `\t` | 탭 | 일정 간격만큼 수평 이동 (Tab) |
| `\\` | 백슬래시 | 문자 `\` 자체를 표현 |
| `\'` | 작은따옴표 | 문자 `'` 자체를 표현 |
| `\"` | 큰따옴표 | 문자 `"` 자체를 표현 |
| `\r` | 캐리지 리턴 | 커서를 현재 줄의 맨 앞으로 이동 |
| `\b` | 백스페이스 | 커서를 한 칸 뒤로 이동 |

### Raw String
```python
# 일반 문자열: \n이 줄바꿈으로 작동
path = "C:\new_folder\test.txt" 

# Raw String: 보이는 그대로 출력
path = r"C:\new_folder\test.txt"
```

### print() 함수 파라미터 활용하기

``` print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)```

| 파라미터 | 기본값 | 기능 설명 | 실무 활용 팁 |
| :--- | :--- | :--- | :--- |
| **`sep`** | `' '` | 여러 인자를 출력할 때 사이사이에 들어갈 구분자를 설정합니다. | CSV 형식(`,`)이나 날짜(`-`) 등을 출력할 때 유용합니다. |
| **`end`** | `'\n'` | 출력이 끝나는 지점에 추가할 문자를 설정합니다. | 기본 줄바꿈을 막고 한 줄로 이어 쓰고 싶을 때 사용합니다. |
| **`file`** | `sys.stdout` | 출력을 표시할 매체(스트림)를 지정합니다. | 화면이 아닌 특정 텍스트 파일에 로그를 기록할 때 사용합니다. |
| **`flush`** | `False` | 버퍼링된 데이터를 즉시 출력할지 결정합니다. | 실시간 진행률 표시나 스트리밍 데이터 출력 시 `True`로 설정합니다. |


```python
# 1. sep 활용: 리스트 요소를 화살표로 연결
print("Python", "Java", "C++", sep=" → ") 
# 결과: Python → Java → C++

# 2. end 활용: 반복문 결과 한 줄로 출력
for i in range(5):
    print(i, end=", ")
# 결과: 0, 1, 2, 3, 4, 

# 3. flush 활용: 실시간 카운트다운 (잠시 대기 없이 즉시 반영)
import time
print("발사 3초 전...", end="", flush=True)
time.sleep(1)

```

### list 값으로 dict 만들기 [ws_2_4]
```python

# 데이터 저장할 빈 dict 생성 
information = dict() # 혹은 information = {}

# 각각 작가와 책 이름이 담긴 리스트
authors = ['김시습', '허균', '남영로', '작자 미상', '임제', '박지원']
books = [
    ['장화홍련전', '가락국 신화', '온달 설화'],
    ['금오신화', '이생규장전', '만복자서포기'],
    ['수성지', '백호집', '원생몽유록'],
    ['홍길동전', '장생전', '도문대작'],
    ['옥루몽', '옥련몽'],
]

# 키와 값을 인덱스 번호 활용해 딕셔너리에 저장
information[authors[0]] = books[1]
information[authors[1]] = books[3]
information[authors[2]] = books[4]
information[authors[3]] = books[0]
information[authors[4]] = books[2]

# f-str 써서 보여주기
for key in information:
    print(f'{key}: {information[key]}')
```

### 깊은 복사와 indexing 접근 [ws_2_5]

1. 얕은 복사
    - 껍데기만 새로 만드는 복사
    - 중첩 리스트 경우, 내용물까지 완전히 새것으로 만들지 못하고 기존의 주소값을 그대로 가져온다. (가장 바깥쪽 리스트는 별개의 객체가 되지만, 그 내부의 참조형 데이터는 원본과 공유한다.)
    - copy() 메서드, 슬라이싱[:], lsit()함수 
2. 깊은 복사
    - 완전한 복제본을 만든다.
    - 중첩 리스트 경우에도 모든 것을 새로 생성하여 독립적인 공간에 저장한다.
    - copy 모듈의 deepcopy()함수

```python
# 도서 목록을 정리하던 중, 제목이 잘못 저장된 경우를 발견하여 수정 후 출력하려고 한다.

catalog = [
    ['시간의 틈', '반짝임의 어둠', '망각의 경계'],
    ['연기의 수수께끼', '장면의 고백', '드라마의 그림자'],
    ['황금의 칼날', '비열한 간신', '무명의 영웅'],
    ['성공의 열쇠', '내면의 변화', '목표의 달성'],
]

# 1. 혹시 모를 사태 대비하여 새로운 변수에 catalog와 같은 값을 할당한다. 얕은 복사로 인한 오류를 범하지 않도록 주의한다.

# map(함수, 반복가능한객체) -> 반복 객체의 각 요소에 이 함수를 모두 적용해줘
# catalog의 요소인 리스트를 하나씩 꺼내어 list()함수를 씌운다.
# 내부의 각 리스트가 새로운 리스트 객체로 복사된다.
# 만약 리스트가 3중 이상으로 겹쳐 있다면 이 방법 또한 앝은 복사 문제가 나타날 것...
# import copy 후, backup_catalog = copy.deepcooy(catalog)로 해결 가능!
backup_catalog = list(map(list, catalog))

# catalog의 3번째 인덱스를 통째로 새로운 리스트로 교체한다.
# 원본은 바뀌었지만, 백업본은 바뀌지 않았다.
# 이런 식으로 통째로 새로운 리스트로 교체하는 경우에는, 위에서 .copy() 등을 통해 얕은 복사를 하더라도, 문제가 발생하지 않는다. 하지만 catalog[3][0] = '성공을 향한 한 걸음' 이런 식으로 내부의 값 하나씩 수정한다면, 얕은 복사 시에 백업본도 같이 변하게 된다. 물론, 지금 위의 복사 방법은 이중 중첩 리스트까지는 깊은 복사에 해당되므로 하나씩 바꾸더라도 안전하다.
catalog[3] = ['성공을 향한 한 걸음', '내 삶의 변화', '목표 달성의 비밀']
''' 
도서 제목 '성공의 열쇠', '내면의 변화', '목표의 달성' 을 각각
'성공을 향한 한 걸음', '내 삶의 변화', '목표 달성의 비밀' 가 되도록 변경하시오.
'''

print('catalog와 backup_catalog를 비교한 결과')
# 식별 연산자로 catalog와 backup_catalog를 비교한 결과를 출력하시오.

print(catalog == backup_catalog)

print('backup_catalog : ')
print(backup_catalog)
print()

print('catalog : ')
print(catalog)
```