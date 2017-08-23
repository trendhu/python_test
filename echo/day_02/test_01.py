class Foo:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def kanchai(self):
        print("%s --- %s --- %s --- 去砍柴"%(self.name, self.age, self.gender))

    def kaiche(self):
        print("%s --- %s --- %s --- 爱开车"%(self.name, self.age, self.gender))

    def zuofan(self):
        print("%s --- %s --- %s --- 想做饭"%(self.name, self.age, self.gender))


xiaoming = Foo('xiaoming', 10, 'nan')
xiaoming.kanchai()
xiaoming.kaiche()
xiaoming.zuofan()









