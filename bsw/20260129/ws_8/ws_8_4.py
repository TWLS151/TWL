class Animal:
    def __init__():
        pass
class Dog(Animal):
    def __init__(self):
        pass
    def bark(self):
        print('멍멍!')
    


class Cat(Animal):
    def __init__(self):
        pass
    def meow(self):
        print('야옹!')
class Pet(Dog, Cat):
    
    def __init__(self, sound):
        self.sound = sound

    def make_sound(self):
        
        print(self.sound)
    def play(self):
        print('애완동물과 놀기')
        


pet1 = Pet("그르르")
pet1.make_sound()
pet1.bark()
pet1.meow()
pet1.play()
