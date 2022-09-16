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


'''show attributes of list and tuple'''
print(dir(mylist))
print("   ")
print(dir(mytuple))
# can find that list is mutable, tuple is immutable


'''An example'''
mylist.remove(2)
print(mytuple)
# print(mytuple.remove(2))  an error occurs to this command


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
