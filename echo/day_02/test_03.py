class Animal:
    
    def eat(self):
        print("%s --> 吃"%self.name)
    
    def drink(self):
        print("%s ---> 喝"%self.name)

    def shit(self):
        print("%s ---> 拉"%self.name)

    def pee(self):
        print("%s ---> 撒"%self.name)

class Cat(Animal):
    
    def __init__(self, name):
        self.name = name
        self.breed = '喵'
    
    def cry(self):
        print("喵喵喵")

class Dog(Animal):
    
    def __init__(self, name):
        self.name = name
        self.breed = '汪'

    def cry(self):
        print("汪汪汪")

cat_1 = Cat('小黑')
cat_1.eat()

cat_2 = Cat('小花')
cat_2.cry()

dog_1 = Dog('二汪')
dog_1.cry()









