
def f1(*args,**kwargs):
    print('the type is', type(args))
    print('the type is', type(kwargs))

f1(1,2)
f1()

print(' ')

dic_zac={'faith': 'Christainity', 'skills':'maths and statistics', 'hobby':'fitness'}

# 定义一个函数来输出dic_zac
def patterns(dic_someone):
    for k,v in dic_someone.items():
        print(k,':',v)
patterns(dic_zac)


print(' ')

# 用kwargs输出dic_zac
def pattern(**kwargs):
    for k,v in kwargs.items():
        print(k,':',v)
pattern(name='Trump',skills='save america',hobby='MAGA')
# 作用：当字典的内容不明晰的时候，可以灵活代入字典形式的参数