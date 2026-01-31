# 아래 클래스를 수정하시오.

class Animal:
    def __init__(self):
        pass

class Cat(Animal):
    def __init__(self):
        super().__init__()
    def meow(self):
        print('야옹!')

cat1 = Cat()
cat1.meow()
