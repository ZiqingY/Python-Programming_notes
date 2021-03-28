'''给list添加元素'''
newlist=[]
for i in range(11):
    newlist.append(i*2)
print(newlist)

'''用一行代码表示'''
print([i*2 for i in range(11)])
print()
# 注：用中括号框起来，说明生成列表

'''提取以大开头的str'''
anotherlist=['大皮皮','小皮皮','大诺诺','小诺诺']
emptylist=[]
for nickname in anotherlist:
    if nickname.startswith('大'):
        emptylist.append(nickname)
print(emptylist)

'''用一行代码表示'''
print([nickname for nickname in anotherlist if nickname.startswith('大')])
