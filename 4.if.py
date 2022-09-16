'''basic if clause'''
a=10
b=20
if b>a:
    print("hello")
if b>1.5*a:
    print("killingspreme")


'''use if, elif, else to construct little programme'''
age=int(input("please enter your age:"))
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
    print("bad liver")
