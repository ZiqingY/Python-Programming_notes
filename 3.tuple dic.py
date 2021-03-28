'''list'''
mylist=[1,2,3,4,5]


'''tuple'''
mytuple=(1,2,3,4,5)
print(type(mylist))
print (type(mytuple))

print(len(mylist))
print(len(mytuple))

print(mytuple[0])
print(mylist[0])


'''查看对list和tuple可行的操作/功能(attribute)'''
print(dir(mylist))
print("   ")
print(dir(mytuple))
# 发现比如list is mutable, tuple is immutable


'''例子'''
mylist.remove(2)
print(mytuple)
# print(mytuple.remove(2))  发现这行代码无法运行


'''Dictionary'''
myDic={"key":"value","key2":"value"}
# example
myPhones={"Iphone X":1000,"Sumsung":900}
print(myPhones)

# access dic keys
Iphone_Price=myPhones["Iphone X"]
print(Iphone_Price)
print("Iphone price: "+str(Iphone_Price))

# change key values
myPhones["Iphone X"]=500
print(myPhones)

myPhones.clear()
print(myPhones)