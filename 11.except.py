'''例1'''
try:
    print(10/0)
except:
    print('you can not do it')


'''例2'''
try:
    print(21/0)
    print(123+"hello")
except ArithmeticError as e:  # 专业的数学报错解释
    print(e)


'''例3'''
try:
    print(21/1)
    print(123+"hello")
except ArithmeticError as e:  # 专业的数学报错解释
    print(e)
except TypeError as a:        # 专业的语法报错解释
    print(a)


'''例4'''
try:
    print(21/1)
    print(123+"hello")
except Exception:              # 自定义报错的内容
    print("you messed it up")
