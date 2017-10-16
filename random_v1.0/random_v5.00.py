"""
    作者：pythonhan
    版本：V4.0
    日期：29/09/2017
    功能：模拟投掷骰子，并输出相应的点数
    2.0新增功能：记录两个骰子的点数和
    3.0新增功能：数据可视化处理
    4.0新增功能： 对数据进行分布情况表示,直方图可视化结果
    5.0新增功能：使用科学计算库，完善程序NumPy
    random模块
    random() 生成[0-1.0）之间的随机浮点数 random.random()
    uniform(a,b) 生成一个a到b之间的随机浮点数
    randint(a,b) 生成一个a 到 b之间的随机整数
    choice(<list>) 从列表中随机返回一个元素
    shuffle(<list>) 将列表中元素随机打乱
    sample(<list>,k) 从指定列表中随机获取k 各元素

    enumerate()函数：同时获取每个元素的索引号及其元素值，用于将可遍历的组合成为一个索引序列
    一般用 for 循环中， 同时列出元素和元素的索引号
    l = ['a','b']
    for x in l:
        print(x)
    for i, x in  enumerate(l):
        print('{}--{}\n'.format(i,x))

    如何将对应的点数和次数关联起来
    zip()函数：拉锁，将两个东西拉到一起，用于将对应的元素打包成一个个tuple
    l1 = [1, 2]
    l2 = [a, b]
    zip(li,l2)
    [(1, 'a'),(2, 'b')] 元组中的元素不可修改，这是一个列表，中间是tuple
    用dict(zip(l1, l2)) 转换成一个dict 就可以修改了

    python数据可视化库

    内置的 matplotlib模块  是一个数据可视化函数库
    matplotlib 的子模块 pyplot 提供了2D 图标制作的基本函数

    散点图的绘制
    import matplotlib.pyplot as plt
#     x,y 分别是x坐标和y坐标的列表
    plt.scatter(x, y)
    plt.show()

    直方图：统计数据
    matplotlib 绘制直方图
     plt.hist(date, bins)
     date:数据列表
     bins:分组边界
     date = [20, 33, 27]
     bins = [0, 10, 20, 30, 40]
     plt.hist(date, bins)

     使用NumPy科学计算库
     1.强大的 n 维数组对象 array
     2.成熟的科学函数库
     3.使用的线性代数、随机数生成函数
     NumPy的操作对象是对维数组 ndarray
     ndarray.shape 数组的维度

     创建数组： np.array(list) , np.arange()
     改变数组形状： reshape()

     NumPy创建随机数组
     np.random.randint(a, b, size)   创建[a,b)间 形状为size的数组
     如：
     import numpy as np
     arr = np.random.randint(1, 10, (3, 4))   #生成1-10之间的数，形状为 3 行 4 列
     print(arr)

     NumPy 也是向量化操作，以数组为对象进行基本运算，加减

     np.histogram() 输出直方图的统计结果
"""
from datetime import datetime
import random
import matplotlib.pyplot as plt
import numpy as np
# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def roll_dice():
    """
    模拟投掷骰子
    """
    roll = random.randint(1,6)
    return roll

def main():
    """
    主函数
    """
    fp = open('random.txt','a')
    name = 'random_v3.00'
    usage = '模拟投掷骰子，并输出相应的点数，2.0新增功能：记录两个骰子的点数和，3.0新增功能：数据可视化处理,可视化投掷两个骰子的结果，5.0科学计算'
    now = datetime.now()
    print('\n \n 当前操作的程序是：{} \n'.format(name), '', end='', file=fp)
    print('该程序的功能为：{} \n'.format(usage), '', end='', file=fp)
    print('您当前操作时间为：{} \n'.format(now), '', end='', file=fp)
    print('此次运行结果为：\n', '', end='', file=fp)

    total_times = 10000

    # 记录骰子1的结果
    roll1_arr = np.random.randint(1, 7, size = total_times)
    roll2_arr = np.random.randint(1, 7, size = total_times)
    result_arr = roll1_arr + roll2_arr

    hist, bins = np.histogram(result_arr, bins = range(2, 14))
    print(hist)
    print(bins)

    #  数据可视化,直方图

    # 指定横坐标每个点的名称
    tick_labels = ['2点', '3点', '4点', '5点',
                   '6点', '7点', '8点', '9点',
                   '10点', '11点', '12点'
                   ]
    # 指定每个点对应的位置
    tick_pos = np.arange(2,13) + 0.5 # 创建数组
    plt.xticks(tick_pos, tick_labels)

    plt.hist(result_arr, bins=range(2,14), normed=1, edgecolor = 'black', linewidth =1, rwidth = 0.8 )  #指定边界颜色和线的宽度,normed=1表示归一化
    # 图片加一个title
    plt.title('骰子点数统计')
    plt.xlabel('点数')
    plt.ylabel('概率')
    plt.show()


    fp.close()

if __name__ == '__main__':
    main()
