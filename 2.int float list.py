'''data type: int'''
a=10
print(type(a))


'''float'''
b=10.5
print(type(b))


'''string'''
name="zacyanneverquit"
print(name[2])
print(len(name))
print(name[2:5])
print(name*2)
print(name+" is true")


'''list'''
mylist=["你好吗", 9, "English", 2020, 2020]
print(type(mylist))
print(len(mylist))
print(mylist[0])
mylist.append(5000)        # adding elements
print(mylist)
mylist.remove(5000)        # delete elements
print(mylist)
print(mylist.count(2020))  # counting elements
