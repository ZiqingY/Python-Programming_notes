# 先从另一个directory import py文件father
from import_practice import father

father.eat()

# 注意这里是从另一个directory import而不是从python package; 且仅仅能import功能，不能import对象

# 例：安装requests：在terminal输入pip install requests，回车
import requests
text=requests.get("http://www.baidu.com")  # 一定要有http
print(text.content)

import random  # impoort module
x=random.randint(1,100)
print(x)

from random import randint # 从module中import部分内容
y=randint(1,4)
print(y)

from math import pi, sqrt #从module中import多个内容
print(pi)

from math import * #从module中import全部内容
z=cos(pi/2)
print(z)

import math
print(math.pi)

import math as zac #对import的对象重新命名，之前的名字无法使用
print(zac.pi)

# python自带的module叫The Standard Library