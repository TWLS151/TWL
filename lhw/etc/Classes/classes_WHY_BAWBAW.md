# 눈이 번쩍 뜨이는 클래스 개념

- 클래스의 개념 중 MOR 개념이라고 해야할지 이해하고 크게 놀랐던 개념을 몇 개 추가합니다.

```python
# 같은 줄에 있다고 같이 처리되는게 아니다.

# 이 문제는 실습실에 있는 문제로 풀이는 어렵지 않지만 개인적으로 놀라운 개념이 숨어있어 따로 코드만 긁어왔습니다.

class Animal:
    pass
    num_of_animal = 0

    def __init__(self):
        pass

class Dog(Animal):
    pass
    sound = '멍멍'

    def __init__(self):
        super().__init__()

    def bark(self):
        print('멍 멍 !')

class Cat(Animal):
    pass
    sound = '야옹'

    def __init__(self):
        super().__init__()

    def meow(self):
        print('야옹!')
        
    def __str__(self):
        return f'애완동물은 {self.sound} 소리를 냅니다.'

class Pet(Dog, Cat):
# class Pet(Cat, Dog):
    pass

    def __init__(self):
        super().__init__()
        
    # def __str__(self):
    #     return f'애완동물은 {self.sound} 소리를 냅니다.'
    
     
pet1 = Pet()
print(pet1) # 애완동물은 멍멍 소리를 냅니다.

cat1 = Cat()
print(cat1) # 애완동물은 야옹 소리를 냅니다.
```
위 코드의 출력이 이상하다는 생각이 들지 않는가?

우선 cat1 은 **str** 매직 매서드가 있으니 출력이 나온다고 치자. 그럼 pet1 은?

pet1 의 매직 메서드는 분명 주석 처리를 해두었는데 cat1 과 같은 출력이 나온다. 왜 그럴까?

위의 코드에
```python
animal1 = Animal()
print(animal1)
```
이 코드를 추가해서 실행해보자
```python
<__main__.Animal object at 0x0000020CFFDA86E0>
```
무슨 에러같은 이상한 출력이 나온다. 이건 에러는 아니고 객체를 출력하려 했지만 클래스에 출력용 메서드가 없기 때문에 객체의 주소가 튀어나온 것이다. id 값이 나왔다고 할 수 있다.

'그래서 어쩌라고'

우리가 매직 메서드 **str** 을 생성하지 않아도 출력을 시도하면 에러가 나지 않고 출력이 된다는 점이 내가 이야기하고 싶은 포인트이다.

> 출력이 있으니까 출력용 메서드가 있으면 사용해서 출력을 해야하는데 출력용 메서드가 없으니 주소가 출력된다.

그럼 그래서 이게 위의 코드랑 무슨 상관일까
```python
pet1 = Pet()
print(pet1) # 애완동물은 멍멍 소리를 냅니다.
```
Pet 클래스를 배정받은 인스턴스 pet1은 str 매직 메서드가 없다.하지만 사용자가 출력을 시도했다. 그러면

> **상위 클래스의 출력용 메서드를 MOR 순서로 탐색한다.**

나는 이 부분이 인상적이었다. 뭐라고? 당연한거 아니냐고? 이거 뿐이었으면 올리지도 않았다.

> 'OK, 그럼 알겠어 출력을 시도하면 출력용 메서드를 탐색해보는구나? 완벽히 이해했어! 넘어가자.. 어? 잠깐만'

## 왜 **멍멍**이지?

왜 멍멍일까? 위에서 코드를 살펴보면 pet1 은 str 메서드가 없기 때문에 MOR 순서대로 탐색해 Dog를 지나 Cat에서 str 메서드를 찾아 출력했다. 그럼 야옹이 되어야하는거 아닌가? 분명 Dog를 지나서 Cat으로 간건데.. 왜 멍멍..

이것도 알고 있으면 인정. 혹시 잘 모르겠고 알고 싶으면 DM!