def add(a,b,c):
    print(a+b+c)
add(1,2,3)


print(' ')
# 用args得到相同结果
def adds(*args):
    print(sum(args))

adds(1,2,3)
adds(1)
adds(1,4,5,6,7,8,8,8,10)


print(' ')

def list(*args):
    print(args)
    print(type(args))
list(1)
list(1,2,3,4,5)

# 作用：可以灵活代入各种形式参数