# 예외 처리, Exception Handling

```python
# try-except

try:
    result = 10 / 0
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
finally:
    print('프로그램이 종료되었습니다.')

try:
    num = int(input('숫자를 입력해주세요: '))
    print('감사합니다.')
except ValueError:
    print('그건 숫자가 아닙니다.')
```

- 간단한 Try - except 구문

 기본적으로 try 안의 내용을 처리하다가 에러가 발생하면 except 파트로 넘어가서 에러를 처리한다.
 정의되지 않은 에러 발생 시 코드가 정지하고 에러 메시지가 팝업된다.

```python
try:
    num = int(input('100을 나눌 값을 입력하시오 : '))
    print(100 / num)
except (ValueError, ZeroDivisionError):
    print('제대로 입력해주세요.')
```
> 하나의 except로 묶는 것도 가능

```python
my_list = []

try:
    number = my_list[1]
except IndexError as error:
    # list index out of range가 발생했습니다.
    print(f'{error}가 발생했습니다.')

    # <class 'IndexError'>가 발생했습니다.
    print(f'{IndexError}가 발생했습니다.')


# import pprint as print
# from pprint import pprint as print
# 모듈을 import할 때 사용하는 as와는 결이 다르다. (다른 as)
```
> as를 이용해 에러를 간단한 구문으로 나타내는 것도 가능하다.
---

## EAFP 방식과 LBYL 방식

```python
my_dict = {
    'key': 'value',
}

# EAFP (Easier to Ask for Forgiveness than Permission)
try:
    result = my_dict['key']
    print(result)
except KeyError:
    print('Key가 존재하지 않습니다.')


# LBYL (Look Before You Leap)
if 'key' in my_dict:
    result = my_dict['key']
    print(result)
else:
    print('Key가 존재하지 않습니다.')
```
> **EAFP** : '일단 박죠?' // **LBYL** : '공략 보고 가죠?'

# 주의사항
```PYTHON
# 아래와 같이 예외를 작성하면 코드는 2번째 except 절에 이후로 도달하지 못함
# ZeroDivisionError 클래스는 Exception 클래스의 하위 클래스 중 하나이므로 ZeroDivisionError를 먼저 작성해야 함
# https://docs.python.org/ko/3/library/exceptions.html#exception-hierarchy
try:
    num = int(input('100으로 나눌 값을 입력하시오 : '))
    print(100 / num)
except Exception:
    print('숫자를 넣어주세요.')
# ZeroDivisionError는 Exception의 하위 클래스이므로 Exception보다 먼저 작성해야 함
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except:
    print('에러가 발생하였습니다.')


# 옳은 코드
# 가장 구체적인 예외부터 처리하고, 마지막에 범용 예외를 처리하도록 순서를 배치
try:
    num = int(input('100으로 나눌 값을 입력하시오 : '))
    print(100 / num)
# 1) 구체적인 예외부터
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except ValueError:
    print('숫자를 넣어주세요.')
# 2) 마지막에 광범위한 예외(Exception)
except Exception:
    print('에러가 발생하였습니다.')
```

 클래스 개념과 MOR 개념을 끌어와보자, 에러를 정의할 때 상위 클래스에 해당하는 에러를 먼저 정의해버리면 MOR 의 시작점을 상위 클래스로 지정해버리는 것. 자연스레 하위 클래스에 해당하는 에러들은 확인해 볼 수가 없다.

> 에러를 정의할 때는 하위 클래스 에러부터 정의해나가야 한다. -> 에러의 클래스 구조를 어느정도 파악해둬야 한다.