class MyClass:
    def instance_method(self):
        return 'instance method', self

    @classmethod
    def class_method(cls):
        return 'class method', cls

    @staticmethod
    def static_method():
        return 'static method'


instance = MyClass()
# 클래스가 할 수 있는 것
# 사실 클래스는 모든 메서드를 호출할 수 있음
print(MyClass.instance_method(instance))
print(MyClass.class_method())
print(MyClass.static_method())


# 인스턴스가 할 수 있는 것
# 사실 인스턴스는 모든 메서드를 호출할 수 있음
print(instance.instance_method())
print(instance.class_method())
print(instance.static_method())


# 기술적인 '가능 여부(Can)'와 논리적인 '사용 의도(Should)'를 구분해야 함
# 1. 클래스의 입장
# - 클래스 메서드와 정적 메서드를 호출하는 것이 주된 역할입니다.
print(MyClass.class_method())
print(MyClass.static_method())

# 2. 인스턴스의 입장
# - 인스턴스 메서드는 오직 인스턴스만 호출하는 것이 좋습니다.
print(instance.instance_method())
