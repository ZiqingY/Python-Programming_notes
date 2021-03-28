class Father:
    def eat(self):
        print("father can eat")


'''继承Father这个object的功能'''
class Son(Father):
    pass
ziqing=Son()
ziqing.eat()
# 输出'father can eat'
print()


'''修改daughter继承的eat功能的输出结果'''
class Daughter(Father):
    def eat(self):
        print("daughter can eat")
wenxue=Daughter()
wenxue.eat()
# 英文叫做overwrite
print()


'''继承多个objects的功能'''
class Mother:
    def sleep(self):
        print("sleeps all day")
class nephew(Father,Mother):
    def eat(self):
        print("nephew can eat")
dick=nephew()
dick.eat()
dick.sleep()