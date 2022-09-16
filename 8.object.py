'''create an object: student'''
class Student():
    def eat(self):
        print("can eat")
    def study(self):
        print("can study")
# def for attributes of the object
Student.eat("self")
Student.eat("啦啦啦")
Student.eat(1234567)  # because the input is set to be N/A, hence any input should generate the same outcome
Student().eat()       # same as above
Student().study()

print()


'''set zac to be an object'''
zac=Student()
zac.eat()
zac.study()


'''everything in Python is an object'''
fruit="apple"
print(fruit.upper())

print()


'''Example：create an object: People'''
class People():
    def pray(self,name):
        print(name + " can pray")
    def read(self,name, frequency):
        print(name+" reads books "+frequency)
People().pray("Zac")
People().read("Zac","everyday")

print()


'''example: create object heroes'''
class heroes():
    name="King Louis"
    country="France"
    def rule(self):
        print(self.name,"rules",self.country)
    @staticmethod  # static: do not need self，but cannot use class variable
    def fight():
        print("King Louis fight for France")
heroes().rule()
heroes().fight()

print()


'''init syntax for input of objects'''
class library():
    def __init__(self, name, source):
        self.name = name
        self.source = source
    def borrow_report(self):
        print(self.name, "borrow a book from",self.source )

student1 = library('Ziqing','University of Bristol')
student1.borrow_report()
student2 = library('Jonny', 'Trinity College')
student2.borrow_report()
# Note: here print() is in the second def, therefore the outcome must come from the second def


