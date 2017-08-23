class Foo:
    def __init__(self, name, blood, damage):
        self.name = name
        self.blood = blood
        self.damage = damage

    def attack(self, otherDamage):
        self.blood = self.blood - otherDamage

    def state(self):
        print("角色：" + self.name + "  ---  剩余血量：" + str(self.blood))
        
soldiers_1 = Foo("xiaoming", 80, 20)

soldiers_2 = Foo("lihua", 100, 10)

soldiers_1.state()

soldiers_1.attack(soldiers_2.damage)

soldiers_1.state()

soldiers_1.attack(soldiers_2.damage * 2)

soldiers_1.state()










