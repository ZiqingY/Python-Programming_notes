'''数据类型int'''
a=10
print(type(a))


'''数据类型float'''
b=10.5
print(type(b))


'''数据类型string'''
name="zacyanneverquit"
print(name[2])
print(len(name))
print(name[2:5])          # 第三个到第五个
print(name*2)
print(name+" is true")


'''数据类型list'''
mylist=["啦啦啦", 9, "English", 2020, 2020]
print(type(mylist))
print(len(mylist))
print(mylist[0])
mylist.append(5000)        # 增加元素
print(mylist)
mylist.remove(5000)        # 删除元素
print(mylist)
print(mylist.count(2020))  # 统计某元素的个数