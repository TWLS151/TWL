# Decorator

```python
# 데코레이터 정의
def my_decorator(func):
    def wrapper():
        # 함수 실행 전에 수행할 작업
        print('함수 실행 전')
        # 원본 함수 호출
        result = func()
        # 함수 실행 후에 수행할 작업
        print('함수 실행 후')
        return result

    return wrapper


# 데코레이터 활용 예시
@my_decorator
def my_function():
    print('원본 함수 실행')


my_function()

my_decorator(my_function())
```
- 함수 안에 함수를 추가할 때 사용하는 함수

 '@'가 데코레이터를 의미하며 @'func' 밑줄에 있는 함수를 'func' 안에 집어 넣는다.

 데코레이터를 직접 만들 일은 거의 없다고 하시니 적당한 이해로 충분할 듯 (존재 여부, 어떻게 작동하는 지 정도)

 --------

 # Magic Method
 ```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    # __str__ 메서드 정의
    # 인스턴스를 문자열로 표현할 때 호출됨
    # print(c1) 호출 시 사용됨
    # 이 메서드를 정의하면 인스턴스를 print()로 출력할 때 더 읽기 쉬운 형식으로 출력됨
    # __str__ 메서드는 문자열을 반환해야 함
    def __str__(self):
        return f'원의 반지름: {self.radius}'
 

c1 = Circle(10)
c2 = Circle(1)

print(c1)  # 원의 반지름: 10
print(c2)  # 원의 반지름: 1
 ```
 - 위의 init / str 이 매직 메서드

print() 를 통해 인스턴스를 출력하려하면 ***str*** 매직 메서드를 찾아 ***MOR*** 순으로 클래스 내부를 순회하고 찾으면 형식대로 출력하고 없다면 제너레이터 형식으로 메모리 주소가 출력 됨

### 추가적인 학습 필요
--------
# Name Space
함수의 스코프 개념이랑 비슷한 것 같음

