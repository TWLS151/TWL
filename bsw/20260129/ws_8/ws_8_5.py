class Animal:
    def __init__(self):
        pass

class Dog(Animal):
    sound = '멍멍'
    def __init__(self):
        pass
    
class Cat(Animal):
    sound = '야옹'
    def __init__(self):
        pass
    
class Pet(Dog, Cat):
    def __init__(self):
        pass
    def __str__(self):
        
        return f'애완동물은 {self.sound} 소리를 냅니다.'

pet1 = Pet()
print(pet1)
        
        





