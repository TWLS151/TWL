## **Control of Flow**  

**제어문(Control Statement)**  
코드의 실행 흐름을 제어하는 데 사용되는 구문  
조건에 따라 코드 블록을 실행하거나 반복적으로 코드를 실행  
1. if문(조건문:참인 경우, 거짓인 경우...)  
if, else, elif ... if만 써도 가능!
2. for문(반복문)  
```python
# for문 작동 원리
item_list = ['apple', 'banana', 'coconut']

for item in item_list:  # item: 반복 변수
    print(item)


# 문자열 순회
country = 'Korea'

for char in country:
    print(char)


# range 순회
for i in range(5):
    print(i)


# for문 dictionary 순회
my_dict = {
    'x': 10,
    'y': 20,
    'z': 30,
}

for key in my_dict:
    print(key)
    print(my_dict[key])


# 인덱스 순회
numbers = [4, 6, 10, -8, 5]

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2

print(numbers)


# 중첩 반복문
outers = ['A', 'B']
inners = ['c', 'd']

for outer in outers:
    for inner in inners:
        print(outer, inner)


# 중첩 리스트 순회
elements = [
    ['A', 'B'], 
    ['c', 'd'],
]

# 1
for elem in elements:
    print(elem)

# 2
for elem in elements:
    for item in elem:
        print(item)

```
3. while 문(반복문-참이면 실행 거짓이면 반복 종료)  
반드시 종료 조건이 필요!  

```python
# while문 기본 1
a = 0

while a < 3:
    print(a)
    a += 1


# while문 기본 2
input_value = ''
while input_value != 'exit':  # exit 를 입력하면 반복 종료
    input_value = input("Enter a value: ")
    print(input_value)


# while문 사용자 입력에 따른 반복
number = int(input('양의 정수를 입력해주세요.: '))

while number <= 0:
    if number < 0:
        print('음수를 입력했습니다.')
    else:
        print('0은 양의 정수가 아닙니다.')

    number = int(input('양의 정수를 입력해주세요.: '))

print('잘했습니다!')

```
4. 반복문 제어 키워드
 - break : 해당 키워드 만나면 남은 코드 무시하고 죽시 종료  
  ```python
# break 키워드 기본
for i in range(10):
    if i == 5:
        break
    print(i)  # 0 1 2 3 4


# break 키워드 예시 (for문)
# 리스트에서 첫번째 짝수만 찾은 후 반복 종료하기
numbers = [1, 3, 5, 6, 7, 9, 10, 11]
found_even = False

for num in numbers:
    if num % 2 == 0:
        print('첫 번째 짝수를 찾았습니다:', num)
        found_even = True
        break

if not found_even:
    print('짝수를 찾지 못했습니다')


# break 키워드 예시 (while문)
# 프로그램 종료 조건 만들기
number = int(input('양의 정수를 입력해주세요.: '))

while number <= 0:
    if number == -9999:
        print('프로그램을 종료합니다.')
        break

    if number < 0:
        print('음수를 입력했습니다.')
    else:
        print('0은 양의 정수가 아닙니다.')

    number = int(input('양의 정수를 입력해주세요.: '))
print('잘했습니다!')
```
 - continue : 해당 키워드 만나면 다음 코드 무시하고 다음 반복을 수행

```python
# continue 키워드 기본
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)  # 1 3 5 7 9


# continue 키워드 예시
# 리스트에서 홀수만 출력하기
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num % 2 == 0:
        continue
    print(num)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    # 만약에 num이 홀수라면 출력 한다.
    if num % 2 == 1:
        print(num)
```
<br>

**map 함수**
```map(function, iterable)```  
반복 가능한 데이터구조의 모든 요소에 함수를 적용하고, 그 결과 값들을 map object로 묶어서 반환  
- map object : 결과를 하나씩 꺼내 쓸 수 있는 반복 가능한 객체 자료형. 전체 값을 확인하려면 list나 tuple로 형변환 해줘야 함  
```python
# map 함수 사용 기본
numbers = [1, 2, 3]
result = map(str, numbers)

print(result)  # <map object at 0x00000239C915D760>
print(list(result))  # ['1', '2', '3']


# map 함수 활용 1 - input과 함께 사용
# 터미널 창에서 1 2 3 입력 (공백 주의)
numbers1 = input().split()
print(numbers1)  # ['1', '2', '3']

## 터미널 창에서 1 2 3 입력 (공백 주의)
numbers2 = list(map(int, input().split()))
print(numbers2)  # [1, 2, 3]


# map 함수 활용 2 - lambda와 함께 사용
numbers = [1, 2, 3, 4, 5]

def square(x):
    return x**2

# lambda 미사용
squared1 = list(map(square, numbers))
print(squared1)  # [1, 4, 9, 16, 25]

# lambda 사용
squared2 = list(map(lambda x: x**2, numbers))
print(squared2)  # [1, 4, 9, 16, 25]

```
<br>

**zip 함수**  
```zip(*iterables)```  
여러 개의 반복 가능한 데이터 구조를 묶어서, 같은 위치에 있는 값들을 하나의 tuple로 만든 뒤 그것들을 모아 zip object로 반환하는 함수  
- zip object : 짝지어진 결과(tuple)를 하나씩 꺼내 쓸 수 있는 반복 가능한 객체 자료형. 전체 값을 확인하려면 list나 tuple로 형변환 해줘야 함  
```python
# zip 함수 사용 기본
girls = ['jane', 'ashley']
boys = ['peter', 'jay']
pair = zip(girls, boys)

print(pair)  # <zip object at 0x000001C76DE58700>
print(list(pair))  # [('jane', 'peter'), ('ashley', 'jay')]


# zip 함수 활용
kr_scores = [10, 20, 30, 50]
math_scores = [20, 40, 50, 70]
en_scores = [40, 20, 30, 50]

for student_scores in zip(kr_scores, math_scores, en_scores):
    print(student_scores)

# zip 함수 활용 (전치 행렬)
scores = [
    [10, 20, 30],
    [40, 50, 39],
    [20, 40, 50],
]

for score in zip(*scores):
    print(score)
```
<br>

**enumerate 함수**  
```enumerate(iterable, start=0)```  
반복 가능 객체의 각 요소에 대해 인덱스와 값을 함께 반환하는 내장함수
```python
# enumerate 함수 기본
fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
    print(index, fruit)
"""
0 apple
1 banana
2 cherry
"""

# enumerate 함수 활용 1
# start 인자를 사용하여 인덱스 번호를 1부터 출력
movies = ['인터스텔라', '기생충', '인사이드 아웃', '라라랜드']

for idx, title in enumerate(movies, start=1):
    print(f"{idx}위: {title}")


# enumerate 함수 활용 2
# 인덱스 정보를 활용하여 특정 조건에 맞는 요소 찾기
respondents = ['은지', '정우', '소민', '태호']
answers = ['', '좋아요', '', '괜찮아요']

for i, response in enumerate(answers):
    if response == '':
        print(f"{respondents[i]} 미제출")
```
<br>

**for else**  
for 루프가 break를 만나 중단되지 않고, 끝까지 정상적으로 완료되었을 때만 else 블록 실행  

```python
# for-else 구문 기본
for i in range(5):
    print(i)
    if i == 3:
        # break 문이 실행되면 else 블록은 실행되지 않음
        print('반복이 중단되었습니다.')
        break
else:
    print('이 메시지는 출력되지 않습니다.')


# for-else 구문 활용 1
# 중복 아이디 찾기 - 찾은 경우
registered_ids = ['admin', 'user01', 'guest', 'user02']
id_to_check = 'guest'  # 이미 리스트에 존재하는 아이디

for existing_id in registered_ids:
    if existing_id == id_to_check:
        print('이미 사용 중인 아이디입니다.')
        break  # 중복 아이디를 찾았으므로 확인 절차를 중단
else:
    # for 루프가 break로 중단되었기에 이 부분은 실행되지 않음
    print('사용 가능한 아이디입니다.')

print('아이디 확인 절차를 종료합니다.')


# for-else 구문 활용 2
# 중복 아이디 찾기 - 찾지 못한 경우
registered_ids = ['admin', 'user01', 'guest', 'user02']
id_to_check = 'new_user'  # 리스트에 없는 새로운 아이디

for existing_id in registered_ids:
    if existing_id == id_to_check:
        print('이미 사용 중인 아이디입니다.')
        break
else:
    # for 루프가 break 없이 마무리 되어 else 블록 실행
    print('사용 가능한 아이디입니다.')

```