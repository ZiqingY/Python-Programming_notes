'''例子：输出type'''
def f1(*args,**kwargs):
    print('the type is', type(args))
    print('the type is', type(kwargs))

f1(1,[2,3])
f1()
# 参数在f1()里无所谓，发现args是tuple, kwargs是dic；说明代入的形式要吻合（tuple和dic的括号省略）
print()


'''定义一个函数来输出字典内容'''
dic_zac={'faith': 'Christainity', 'skills':'maths and statistics', 'hobby':'fitness'}

def patterns(dic_someone):
    for k,v in dic_someone.items():
        print(k,':',v)
# for key and value in...
patterns(dic_zac)


print()
''' 用kwargs输出字典内容, 当字典的内容不明晰的时候，可以灵活代入字典形式的参数 '''
def pattern(**kwargs):
    for k,v in kwargs.items():
        print(k,':',v)
pattern(name='Trump',skills='save america',hobby='MAGA', achievement='inspire us')