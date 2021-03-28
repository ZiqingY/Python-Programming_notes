def fun1():
    print ("hello world")
fun1()

def fun2(x,y):
    print(x*y)
fun2(2,10)
fun2(100,6)

def fun3(x,y):
    return(x**3+y**2)  # 不会打印出来
a=fun3(1,2)
print(a)

def converter(weight):
    ponds=weight/0.45
    print(ponds)
converter(83)

def converter2(weight=100):
    ponds=weight/0.45
    print(ponds)
converter2()
converter2(weight=5000)