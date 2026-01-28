# class

## 클래스란?
- 객체를 만들기 위한 설계도(blueprint)
- 데이터(속성)와 기능(메서드)을 하나로 묶어서 관리

## 기본 문법

```python
class Person:
    # 생성자: 객체가 만들어질 때 자동 호출
    def __init__(self, name, age):
        self.name = name  # 인스턴스 속성
        self.age = age

    # 인스턴스 메서드
    def greet(self):
        print(f"안녕하세요, {self.name}입니다.")

# 객체(인스턴스) 생성
p1 = Person("철수", 25)
p1.greet()  # 안녕하세요, 철수입니다.
```

## self란?
- 인스턴스 자기 자신을 가리킴
- 메서드의 첫 번째 매개변수로 반드시 작성
- 호출할 때는 자동으로 전달됨

## 클래스 변수 vs 인스턴스 변수

```python
class Dog:
    species = "포유류"  # 클래스 변수 (모든 인스턴스가 공유)

    def __init__(self, name):
        self.name = name  # 인스턴스 변수 (각 인스턴스마다 별도)

dog1 = Dog("멍멍이")
dog2 = Dog("바둑이")

print(Dog.species)   # 포유류
print(dog1.species)  # 포유류
print(dog1.name)     # 멍멍이
print(dog2.name)     # 바둑이
```

## 상속

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Cat(Animal):  # Animal 클래스 상속
    def speak(self):
        return f"{self.name}: 야옹"

class Dog(Animal):
    def speak(self):
        return f"{self.name}: 멍멍"

cat = Cat("나비")
print(cat.speak())  # 나비: 야옹
```

## 매직 메서드 (던더 메서드)

| 메서드 | 설명 |
|--------|------|
| `__init__` | 생성자, 객체 초기화 |
| `__str__` | print() 출력 형태 정의 |
| `__repr__` | 객체의 공식적 문자열 표현 |
| `__len__` | len() 호출 시 동작 |
| `__eq__` | == 비교 연산 |

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1)        # Point(1, 2)
print(p1 == p2)  # True
```

## 캡슐화

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # __로 시작하면 private

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # 1500
# print(account.__balance)    # AttributeError 발생
```

## 정리
- `class`: 객체의 설계도
- `__init__`: 생성자
- `self`: 인스턴스 자신
- 상속으로 코드 재사용
- `__`로 시작하는 속성은 외부 접근 제한
