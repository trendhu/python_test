class Test:
    def prt(self):
        print(self)
        print(self.__class__)
        print(type(self))
#self 代表的是类的实例，代表当前对象的地址，而 self.class 则指向类。
#类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self
#self 不是 python 关键字，我们把他换成 runoob 也是可以正常执行的:
#我们使用 self 只是因为习惯
t = Test()
t.prt()









