'''从father.py import father这个对象'''
import father
father.eat()

# 如果是从另一个directory import（而不是从python package），用from import
# 且仅仅能import功能（def），不能import对象


'''从网上down module例：安装requests：在terminal输入pip install requests，回车'''
import requests
text=requests.get("http://www.baidu.com")  # 一定要有http
print(text.content)

import random                         # import module
x=random.randint(1,100)
print(x)

from random import randint            # 从module中import部分内容
y=randint(1,100000)
print(y)

from math import pi, sqrt             # 从module中import多个内容
print(pi, sqrt(pi))

from math import *                    # 从module中import全部内容
z=cos(pi/2)
print(z)

import math
print(math.pi)

import math as zac # 对import的对象重新命名，之前的名字无法使用
print(zac.pi)

                   # python自带的module叫The Standard Library