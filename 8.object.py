'''创建一个Student的对象'''
class Student():
    def eat(self):
        print("can eat")
    def study(self):
        print("can study")
# def定义对象属性
Student.eat("self")
Student.eat("啦啦啦")
Student.eat(1234567)  # 因为对象参数为空，所以任何参数都得到相同结果
Student().eat()       # 此行和上面一样
Student().study()

print()


'''给变量zac赋值为对象'''
zac=Student()
zac.eat()
zac.study()


'''python里的任何东西都是对象，例如string也是对象'''
fruit="apple"
print(fruit.upper())

print()


'''例：创建对象People，属性含参数'''
class People():
    def pray(self,name):
        print(name + " can pray")
    def read(self,name, frequency):
        print(name+" reads books "+frequency)
People().pray("Zac")
People().read("Zac","everyday")

print()


'''例：创建对象heroes，属性含class变量和参数'''
class heroes():
    name="Trump"
    country="America"
    def save(self):
        print(self.name,"saves",self.country)
    @staticmethod  # 静态属性: 不用带self，但不能引用class variable
    def fight():
        print("Trump fights for America")
heroes().save()
heroes().fight()

print()


'''init使得object的功能可以代入参数'''
class swamp():
    def __init__(self, name, source):
        self.name = name
        self.source = source
    def corrupt_report(self):
        print(self.name, "takes bribes from",self.source )

swamp1 = swamp('jeobiden','China')
swamp1.corrupt_report()
swamp2 = swamp('Barack Obama', 'White Left')
swamp2.corrupt_report()
# 注：这里print再第二个def的属性里，所以要输出结果必须执行第二个属性


