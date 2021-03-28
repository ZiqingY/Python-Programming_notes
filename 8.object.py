
class Student():
    def eat(self):
        print("can eat")
    def study(self):
        print("can study")

Student.eat("self")
Student.eat("啦啦啦")
Student.eat(1234567)
Student().eat()   # 此行和上面一样
Student().study()

print("                ")

# 给变量赋值成特定对象
zac=Student()
zac.eat()
zac.study()

# python里的任何东西都是对象，例如string也是对象：
fruit="apple"
print(fruit.upper())

print("                ")

class People():
    def pray(self,name):
        print(name + " can pray")
    def read(self,name, frequency):
        print(name+" reads books "+frequency)
People().pray("Zac")
People().read("Zac","everyday")

print("                ")

class heroes():
    name="Trump"
    country="America"
    def save(self):
        print(self.name,"saves",self.country)
    @staticmethod  # 不用带self，但不能使用class variable
    def fight():
        print("Trump fights for America")
heroes().save()
heroes().fight()

print("                ")


# init使得object的功能可以代入参数
class swamp():
    def __init__(self,name,source):
        self.name=name
        self.source=source
    def corrupt(self):
        print(self.name, "takes bribes from",self.source )
swamp1=swamp('jeobiden','China')
swamp1.corrupt()



