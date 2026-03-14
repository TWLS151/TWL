# Code for Classes

```python
class name_class: # 클래스 명 정의 및 선언
    
    # 클래스 변수 (모든 인스턴스가 공유하는 정보)
    class_value = value

    # 생성자 메서드 생성 (__init__은 생성자 메서드이며 매직 메서드)
    def __init__(self, a, b): # self 는 default값이고 a, b는 인스턴스 변수 (각 인스턴스 고유의 값)
        self.a = a
        self.b = b
        pass

    def instance_method(): # 클래스에 속해있는 인스턴스만 사용할 수 있는 메서드 생성
        pass

    @classmethod
    def classes_method(): # 클래스의 모든 하위 객체가 사용할 수 있는 메서드 생성 (상속 받은 인스턴스 포함)
        pass

    @staticmethod
    def static_method(): # 클래스의 모든 하위 객체가 사용할 수 있지만 각 클래스나 객체의 변수에는 영향을 주지 않는 스태틱 메서드 생성
        pass




name = name_class() # 인스턴스 생성

print(name.a) # name 인스턴스의 a 인스턴스 변수 접근

print(name.class_value) # name 인스턴스가 속해 있는 클래스 변수 접근
print(name.instance_method()) # name 인스턴스가 속해있는 클래스의 instance_method 메서드 호출

print(name.classes_method()) # name 인스턴스가 속해있는 클래스의 클래스 메서드 classes_method 호출

print(name_class.static_method()) # class 에 있는 스태틱 메서드 static_method() 호출 // 주로 데이터 변화를 요구하지 않는 단순한 계산, 참 거짓 판단에 사용함 (하단부 예시)



```

[static_method_ex](/static_method_ex.py)
[method_role](/method_role.py)