2017年10月23日
基础知识学习部分：
1.	普通代码保存为.py, GUI程序保存为.pyw文件
2.	常用快捷键：
F1	打开帮助文档
Alt + / 	自动补全
Ctrl + ] 	缩进代码块
Ctrl + [	取消代码块缩进
Alt + 3   注释代码块
Alt + 4	取消代码块注释
Pip install SomePackage
（命令行）Pip list 显示已安装所有模块
Pip install –upgrade SomePackage 	升级模块
Pip uninstall somepackage 		卸载模块
Pip install somepackage.whl 	使用whl文件直接安装some package
直接安装应从cmd窗口先进入文件夹，然后把安装文件放入该文件夹，再运行命令安装
Cd 文件夹
Pip install a.whll
3.	python 中的一切都是对象。变成单元类型有函数和类。对象类型还有tuple, list, dict. tuple类型不可以查看某个位置的元素值。
4.	在python中，不需要实现声明变量名及其类型，直接赋值即可创建各种类型，python是一种动态类型语言，变量的类型是可以随时变化的。
5.	Python中允许多个变量指向同一个值。数字属于python中的不可变对象。修改整型类型的值的时候并不是真的修改变量的值，而是先把值存放到内存中，然后修改变量使其指向了新的内存地址。其他类型也一样。
6.	id（x）返回x所指的值的内存地址，python采用的是基于值的内存管理方式，如果为不同变量赋值为相同值，这个值在内存中只有一份，多个变量指向同一块内存地址。Python具有自动内存管理功能，会跟踪所有的值，并自动删除不再有变量指向的值。因此，python程序员一般情况下不需要太多考虑内存管理的问题。
7.	（1）变量名必须以字母或者下划线开头，但是下划线开头的变量在python中有特殊的含义
（2）变量名中不能有空格以及标点符号
（3）不能使用关键字作为变量名，可以导入keyword模块后使用print(keyword, kwlist )查看所有python关键字
Import keyword
Keyword.kwlist
(4)不建议使用系统内置模块名，函数名类型名等，因为这将会改变其类型和含义。dir(__builtins__)查看所有内置模块、类型和函数。
（5）变量名区分应为字母的大小写。
8  python中数值类型主要有，整数，浮点数和复数。复数用j或者J来表示虚部
	a.real	#查看复数实部
	a.imag	#查看复数虚部
	a.conjugate()	#返回共轭复数
	a * b, a / b	#复数乘除
9.	字符串使用支持+运算符合并来生成新字符串，可以对字符串进行格式化，把其他类型对象按照格式要求转换为字符串，并返回结果字符串，如
a = 3.994559
‘%7.3f’% a
‘    3.994’
10.	Python支持转义字符，字符串前面加r或者R表示原始字符串，其中特殊字符不进行转义
\n 换行符
\t 制表符
\r 回车
\’单引号
\”双引号
\\ 一个\
\ddd 3位8进制数对应的字符
\xhh 2位十六进制数对应的字符
11.	特殊运算符：
X // y 求整商
X ** y 幂运算
‘x’% y 既可以求余数，也可以格式化字符串
or and not in
位运算符： | ^ & << >> ~
集合交并补： & 	| 	^
矩阵乘法： 	@
12.	*的特殊用法：
‘1’* 5 		表示’11111’字符串重复
[1, 2, 3] * 2		表示列表重复
13.	Python中，单个任何类型对象或者常数属于合法表达式，使用连接符的组合也为合法表达式
a = [1]
b = [2]
a + b 		输出为[1, 2]
d = list (map(str, a+b)) 	输出为[‘1’,’2’]
,为普通分隔符
x = 3, 5
(3, 5)
14. python3.5以上添加了矩阵相乘运算符，
import numpy
x = numpy.ones(3)   #ones()函数用于生成全1矩阵，参数表示矩阵大小
m = numpy.eye(3) * 3 #eye()函数用于生成单位矩阵
m[0, 2]     #访问矩阵指定位置元素的值
x @ m   矩阵乘法
15.常用内置函数
abs(x)      #绝对值
all(iterable)       #全部可迭代对象均为True，则返回Ture
any(iter)           #只要有True，返回True
bin(x)              #转换成二进制
callable(object)    #测试对象是否可调用
chr(x)              #返回ASCII编码(python2)或者unicode编码（python3)的字符
ord(s)          #返回字符s的ASCII编码(p2)或者Unicode编码（p3）
cmp(x, y )          #比较大小，x < y ，返回负数，x == y ，返回0， x >  y,返回正,python3不支持
dir(x)              #返回制定对象或者模块的成员列表
eval(s[, globals[, locals]])        #计算字符串中表达式的值并返回
filter(function or None, sequence)  #返回序列中使得函数值为True的那些元素，
float(x)            #数字或者字符串转换为浮点数并返回
help(obj)
hex(x)              #转换成16进制
id(obj)             #返回操作对象地址
input([提示内容])   #Python2和python3该函数不同
int(x[,d])          #返回数字的整数部分，或者把d进制的字符串x转换为十进制并返回,d默认为10
isinstance(object, class or type or tuple)      #测试对象是否属于指定类型的实例
len(obj)            #返回字符串长度
list([x]),set([x]),tuple([x]),dict([x])     #被对象转换为列表，集合，元祖或者字典并返回
map(函数，序列)      #将但参数函数映射到序列中的每个元素,返回结果列表(p2)或者map对象(p3)
max(x),min(x),sum(x)
oct(x)          #数字x转换成八进制字符串
open(name)      #指定模式打开文件
pow(x, y )      #x 的 y 次方
range(start, end, step)     #返回等差数列列表，不包括终值，p3返回range对象
reduce(函数，序列)           #将接受2个参数的函数以累积的方式从左到右依次应用到序列中每个元素，最终返回单个值作为结果
round(x, 小数位数)      #四舍五入，若不指定小数位数，返回整数
str(x)                  #变成字符串
sorted(list)            #返回排序后结果
type(x)                 #返回类型
zip(序列)               #返回[序列]形式的列表(p2)或者zip对象(p3)

16 ord() 和 chr() 函数功能相反,作用于单个字符，str()将任意类型参数转换为字符串
ord('a')
chr(66)
chr(ord('a') + 1)
str({1, 2, 3})

17 max() min() sum() 三个内置函数作用于计算列表，tuple,或者其他可以迭代对象中所有元素的值，sum()只支持包含数值型元素的序列或者可迭代对象，max()和min()要求可迭代对象或者序列可以比较大小
import random
a = [random.randint(1, 100) for i in range(10)]
print(max(a), min(a), sum(a))
# 若要计算平均值
sum(a) * 1.0 / len(a)   python2
sum(a) / len(a) python 3
# 得到结果一样，都是小数

18 dir()函数查看可操作对象，help()查看用法

19.对象的删除，可以使用del 命令显示删除对象并解除其和值之间的指向关系。删除对象时，如果有别的变量指向该值，则不删除该值，如果删除对象后该值不再有其他变量
指向，则删除该值。
x = [3]
y = 3
del y
del x[0]
del x
del命令无法删除tuple或者字符串中的指定元素，而只可以删除整个元组或者字符串，因为这两个都属于不可变序列。

20 基本输入输出
输入 ： x = input('提示：')           #该函数返回用户输入的对象
python2 和python3 解释不同：
python2:
 >>>   x = input('please input: ')
    please input: 3     #没有界定符号，整数
 >>>print type(x)
 <type 'int'>
 >> > x = input('please input: ')
please input: '3'  # 字符串
>> > print type(x)
< type 'str'>
即输入什么类型就是什么类型
 raw_input()也可以接受用户值，但是raw_input()函数返回的结果类型均为字符串，不论用户使用什么界定符
python3：
这里不存在raw_input()函数，只有input()函数，不论输入使用什么界定符，input()函数返回结果都是字符串，需要将其转换成相应的类型在处理
>>> x = input('please input: ')
please input: 3  # 没有界定符号，整
>>> print type(x)
< type 'str'>

输出也不一致，python2使用print语句输出，python3使用print()函数输出
输出结果到指定文件操作也不同：
python 2:
>>> fp = open(r'e:\practice\mytest.txt', 'a+')
>>> print >> fp, "hello, world"
>>> fp.close()
python 3:
>>> fp = open(r'e:\pracice\mytest.txt', 'a+')
>>> print('hello world', file = fp)
>>> fp.close()
另外一个不同，python2中在print语句后边加上','，表示输出内容之后不换行
>>> for i in range(2):
    print i,
0 1
python 3:
>>> for i in range(2):
    print(i,end = '')
0 1

21. 模块导入与使用
import math
import random
x = random.random()   #生成[0, 1)内的随机小数
n = random.randint(1, 100) #生成[1, 100)内的随机整数
import numpy as np
a = np.array((1, 2, 3)) #通过模块别名来访问对象
from math import sin
sin(30)
from math import sin as f
f(30)
from math import *      #表示从math一次导入模块中的所有对象，不推荐使用，以免发生混乱
python 2 用reload() 来重新导入一个模块，而python 3 中需要使用imp模块或者importlib模块的reload()函数
模块导入顺序：
(1)导入python标准库模块，如os, sys, re
(2)导入第三方扩展库，如PIL， numpy, scipy
(3)导入本地模块

21.python 代码编写规范：
(1)缩进很重要，一般以4个空格为基本缩进单位。ctrl + / 进行代码块注释，选中代码块也可以直接tab缩进
(2)注释：# 或者 """……""" 或者''' '''被认为是注释
(3)每个import语句只导入一个模块，尽量避免一次导入多个模块

22.python文件名：
(1)py:python源文件，由python解释器负责解释执行
(2)pyw:python源文件，常用于图形界面程序文件
(3)pyc:python字节码文件，无法使用文本编辑器直接查看，可用于隐藏python源代码和提高运行速度，在模块第一次导入时会被编辑成pyc，提高运行速度和加载速度，
(4)pyd:一般由其他语言编写并编译的二进制文件，常用于实现某些软件工具的python编程接口插件，或者Python动态链接库。

23.python脚本的__name__属性
如果脚本作为模块被导入，那么__name__属性的值被自动设置为模块名；
如果脚本独立运行，那么__name__属性的值会被设置为'__main__'
利用__name__属性可以控制python程序的运行方式，一个编写了包含大量函数的模块，不希望这个模块可以直接运行，可以添加下面代码
if __name__ == '__main__':
    print('please use me as a module')

24.编写自己的包，包的每个目录中必须包含一个__init__.py文件，是一个空文件，只是用来表示这是一个包
__init__.py 文件的主要用途是设置 __all__变量以及执行初始化包所需的代码，__all__变量中定义的函数才可以被正确导入：
如果有以下包：
sound/
    __init.py
    formats/
            __init__.py
            wavread.py
    effects/
            __init__.py
            echo.py
    filters/
            __init__.py
            vocoder.py
则可以在自己的程序中导入其中一个模块
import sound.effects.echo
然后来调用其中的成员


practice

1.输入一个三位数，计算并输出其每个数字
x_str = input('请输入一个三位数：')
x = eval(x_str)
a = x // 100
b = x //10 % 10
c = x % 10
print(a, b, c)

2.已知三角形两边长和夹角，求第三边长
import math
x = input('输入两边长和夹角，用逗号隔开：')
a,b,theta = map(float, x.split(','))
c = math.sqrt(a + b +theta)
print('c= {}'.format(c))
print('c= %5.2f' % c)

3.任意输入三个英文单词，按照字典顺序输出
s = input('请输入三个英文字符，用逗号隔开：')
x, y, z = s.split(',')
x, y, z = sorted([x, y, z])
print('x,y,z分别是{},{},{}'.format(x, y, z))
print(x, y, z)