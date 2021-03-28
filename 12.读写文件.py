# 打开此路径的文件，解码中文
file= open('zac.txt', encoding='UTF-8')
text=file.read()
print(text)
file.close()

# 打开此路径文件
file2=open('zacEn.txt')
text2=file2.read()
print(text2)
file2.close()

# with open不用close(), 更常用
with open ('zac.txt','r',encoding='UTF-8') as Z:
    print(Z.read())

# 打开非此路径的文件
file3=open('/Users/Altair/PycharmProjects/zac3.txt')
text=file3.read()
print(text)
file3.close()

# 写文件
# with open('zac4.txt','w') as x:  # 新撰写内容
#     x.write('hello world, i love u')
# with open('zac4.txt','a') as x:  # 补充内容
#     x.write('    ahhhhh')


# 往下一行接着写
with open('zac4.txt','a') as x:
    x.write('to be continued\n')
with open('zac4.txt','a') as x:
    x.write('to be continued\n')