'''基本if语句'''
a=10
b=20
if b>a:
    print("hello")
if b>1.5*a:
    print("killingspreme")


'''通过if elif else构建判断小程序'''
age=int(input("please enter your age:"))  # 需要手动在output栏输入参数
print(type(age))

if age<18:
    print("you can not drink")
elif age==18:
    print('you can not drink either')
elif 50>age>=19:
    print("you can not drink still")
elif 100>age>50:
    print("you can not drink as always")
else:
    print("you die")