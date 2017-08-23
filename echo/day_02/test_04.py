class D:
    def bar(self):
        print("D.bar")

class C(D):
    def bar(self):
        print("C.bar")

class B(D):
    def bar2(self):
        print("B.bar")

class A(B, C):
    def bar1(self):
        print("A.bar")

a =A()
a.bar()

#下方知识未被验证成功
# 经典类：首先去A类中查找，如果A类中没有，则继续去B类中找，如果B类中么有，则继续去D类中找，如果D类中么有，则继续去C类中找，如果还是未找到，则报错

# 新式类：首先去A类中查找，如果A类中没有，则继续去B类中找，如果B类中么有，则继续去C类中找，如果C类中么有，则继续去D类中找，如果还是未找到，则报错

# 注意：在上述查找过程中，一旦找到，则寻找过程立即中断，便不会再继续找了










