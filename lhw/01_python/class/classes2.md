# Advanced Classes

### 상속, Inheritance
- 클래스가 인스턴스를 가지듯이 클래스도 클래스에 소속될 수 있음.

상위 클래스가 인스턴스에게 클래스 변수를 제공하듯이 하위 클래스는 상위 클래스에게 클래스 변수를 제공 받을 수 있으며 하위 클래스 또한 하위 클래스를 가질 수 있고 인스턴스 또한 가질 수 있다.

```python
class Object:
    def shoot(self):
        print('shoot')

class Animal(Object):
    def eat(self):
        print('먹는 중')


class Dog(Animal):
    def bark(self):
        print('멍멍')



my_dog = Dog()

my_dog.bark()  # 멍멍

my_dog.shoot() # shoot

# 부모 클래스(Animal) 메서드 사용 가능
# 먹는 중
```
- 클래스가 상위 클래스를 가진다는 정보는 클래스 선언 시 클래스 명 옆에 **소괄호**로 표시
- Dog 는 Animal의 하위 클래스이고 Animal 은 Object의 하위 클래스

> `1번 파일에 넣어둔 조직 구성도 참조`

---

### 다중 상속, Multiple Inheritance

- 하나의 클래스가 여러 상위 클래스를 가질 수 있음
```python
class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return f'안녕, {self.name}'


class Mom(Person):
    gene = 'XX'

    def swim(self):
        return '엄마가 수영'


class Dad(Person):
    gene = 'XY'

    def walk(self):
        return '아빠가 걷기'


class FirstChild(Dad, Mom):
    def swim(self):
        return '첫째가 수영'

    def cry(self):
        return '첫째가 응애'


baby1 = FirstChild('아가')
print(baby1.cry())  # 첫째가 응애
print(baby1.swim())  # 첫째가 수영
print(baby1.walk())  # 아빠가 걷기
print(baby1.gene)  # ??
print(baby1.greeting())
```
가장 하위 클래스인 FirstChild는 Dad 클래스와 Mom 클래스를 상속 받았다.

 이 때 두 상위 클래스가 공통적으로 가지는 클래스 변수의 경우 같은 이름의 변수가 두 개가 입력되는데 이런 경우 먼저 상속받은 클래스 Dad 의 변수가 살아남는다.

 또한 하위 클래스가 갖고 있지 않는 변수나 메서드를 하위 클래스 객체가 접근하게 되면 **MOR** 을 따라 상위 클래스를 탐색하며 해당 변수나 메서드를 찾게 되는데 단축 실행처럼 목표를 찾게 되면 바로 과정을 종료하고 해당 목표를 사용한다.

 > print(baby1.greeting()) 에서 FirstChild 의 인스턴스인 baby1 은 greeing() 메서드를 갖고 있지 않기에 상위 클래스를 탐색하며 찾은 Person의 greeting() 메서드를 사용하게 됨. 출력은 '안녕, 아가'

 ---

 ### Super()

 클래스에 속해 있는 모든 클래스, 인스턴스들이 가지는 정보이지만 그 정보의 내용은 모두 다 다른 경우 (ex. 이름) 클래스 변수로 획일화 할 수 없다.

 그런 경우 변수의 이름은 모두 다 같지만 값만 다르게 설정해야 하지만 .super() 메서드를 활용하면 손쉽게 상위 메서드의 인스턴스 변수명을 가져올 수 있다.

 ```python
# 다중 상속
class ParentA:
    def __init__(self):
        super().__init__()
        self.value_a = 'ParentA'

    def show_value(self):
        print(f'Value from ParentA: {self.value_a}')


class ParentB:
    def __init__(self):
        self.value_b = 'ParentB'

    def show_value(self):
        print(f'Value from ParentB: {self.value_b}')


class Child(ParentA, ParentB):
    def __init__(self):
        super().__init__()  # ParentA 클래스의 __init__ 메서드 호출
        self.value_c = 'Child'

    def show_value(self):
        super().show_value()  # ParentA 클래스의 show_value 메서드 호출
        print(f'Value from Child: {self.value_c}')


child = Child()
child.show_value()
"""
Value from ParentA: ParentA
Value from Child: Child
"""

print(child.value_c)  # Child
print(child.value_a)  # ParentA
print(
    child.value_b
)  # AttributeError: 'Child' object has no attribute 'value_b'


"""
<ParentA에 super().__init__()를 추가하면?>
그 다음으로 ParentB의 __init__가 실행되어 value_b도 초기화할 수 있음
그러면 print(child.value_b)는 ParentB를 출력하게 됨

print(child.value_b)  # ParentB
"""

"""
<Child 클래스의 MRO>
Child -> ParentA -> ParentB

super()는 단순히 “직계 부모 클래스를 가리킨다”가 아니라, 
MRO 순서를 기반으로 “현재 클래스의 다음 순서” 클래스(또는 메서드)를 가리킴

따라서 ParentA에서 super()를 부르면 MRO상 다음 클래스인 ParentB.__init__()가 호출됨
"""


"""
1.1 Child 클래스의 인스턴스를 생성할 때 일어나는 일
    1.	child = Child() 호출 시, Child.__init__()가 실행
    2.	Child.__init__() 내부에서 super().__init__()를 호출
        - 여기서 Child의 super()는 MRO에 의해 ParentA의 __init__()를 가리킴
    3.	ParentA.__init__()로 진입

1.2. ParentA.__init__() 내부
	1.	ParentA.__init__()에는 다시 super().__init__()가 있음
	2.	ParentA를 기준으로 MRO에서 “다음 클래스”는 ParentB, 따라서 ParentA의 super().__init__()는 ParentB.__init__() 호출
    3.	ParentB.__init__()가 실행되면서 self.value_b = 'ParentB'가 설정됨
	4.	ParentB.__init__()가 종료된 후, 다시 ParentA.__init__()로 돌아와 self.value_a = 'ParentA'가 설정됨
	5.	ParentA.__init__() 종료 후, 다시 Child.__init__()로 돌아감
	6.	마지막으로 Child.__init__() 내에서 self.value_c = 'Child'가 설정되고 종료

1.3 결과적으로 child 인스턴스는 value_a, value_b, value_c 세 속성을 모두 갖게 됨
	- child.value_a → 'ParentA'
	- child.value_b → 'ParentB' 
	- child.value_c → 'Child'
"""
 ```