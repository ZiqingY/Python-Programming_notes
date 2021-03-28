try:
    print(10/0)
except:
    print('you can not do it')

try:
    print(21/0)
    print(123+"shit")
except ArithmeticError as e:  #专业的数学报错解释
    print(e)

try:
    print(21/1)
    print(123+"shit")
except ArithmeticError as e:  #专业的数学报错解释
    print(e)
except TypeError as a:  #专业的语法报错解释
    print(a)

try:
    print(21/1)
    print(123+"shit")
except Exception:  #自定义报错的内容
    print("you fucked it up")