class Foo:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def detait(self):
        print(self.name, self.age)

obj1 = Foo('zhangsan', 18)
# print(obj1.name)
# print(obj1.age)
obj1.detait()   # Python默认会将obj1传给self参数，即：obj1.detail(obj1)，所以，此时方法内部的 self ＝ obj1，即：self.name 是 wupeiqi ；self.age 是 18

obj2 = Foo('lisi', 73)
# print(obj2.name)
# print(obj2.age)






