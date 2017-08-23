class Employee:
    '所有员工的基类'
    empCount = 0    #全局变量，属于整个类

    def __init__(self, name, salary):
        self.name = name    #属性，仅属于当前实例对象
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name:" + self.name, "Salary:" + str(self.salary))

a = Employee("xiaoming", 5000)
a.displayCount()
a.displayEmployee()

b = Employee("lihua", 7500)
b.displayCount()
b.displayEmployee()

c = Employee("chenglu", 300)
c.displayCount()

print(Employee.empCount)


print(" --------------------------------------------")

print(hasattr(b, 'name'))
print(getattr(b, 'name'))
print(hasattr(b, 'age'))
setattr(b, 'age', 45)
print(b.age)
delattr(b, 'age')
print(hasattr(b, 'age'))


# 你可以添加，删除，修改类的属性，如下所示：
# emp1.age = 7  # 添加一个 'age' 属性
# emp1.age = 8  # 修改 'age' 属性
# del emp1.age  # 删除 'age' 属性



# 你也可以使用以下函数的方式来访问属性：
#     getattr(obj, name[, default]) : 访问对象的属性。
#     hasattr(obj,name) : 检查是否存在一个属性。
#     setattr(obj,name,value) : 设置一个属性。如果属性不存在，会创建一个新属性。
#     delattr(obj, name) : 删除属性。



# Python内置类属性
#     __dict__ : 类的属性（包含一个字典，由类的数据属性组成）
#     __doc__ :类的文档字符串
#     __name__: 类名
#     __module__: 类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
#     __bases__ : 类的所有父类构成元素（包含了一个由所有父类组成的元组）


# Python同样支持运算符重载(见 http://www.runoob.com/python/python-object.html )






