"""
    作者：pythonhan
    版本：V3.0
    日期：29/09/2017
    功能：模拟投掷骰子，并输出相应的点数
    2.0新增功能：记录两个骰子的点数和
    3.0新增功能：数据可视化处理
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

"""
from datetime import datetime
import random
import matplotlib.pyplot as plt

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
    usage = '模拟投掷骰子，并输出相应的点数，2.0新增功能：记录两个骰子的点数和，3.0新增功能：数据可视化处理,可视化投掷两个骰子的结果'
    now = datetime.now()
    print('\n \n 当前操作的程序是：{} \n'.format(name), '', end='', file=fp)
    print('该程序的功能为：{} \n'.format(usage), '', end='', file=fp)
    print('您当前操作时间为：{} \n'.format(now), '', end='', file=fp)
    print('此次运行结果为：\n', '', end='', file=fp)

    total_times = 100
    # 初始化总数列表[0, 0, 0, 0, 0, 0]
    result_list = [0] * 11
    # 初始化点数列表
    roll_list = list(range(2,13))

    roll_dict = dict(zip(roll_list, result_list))

    # 记录骰子1的结果
    roll1_list = []
    roll2_list = []


    for i in range(total_times):
        roll1 = roll_dice()
        roll2 = roll_dice()

        roll1_list.append(roll1)
        roll2_list.append(roll2)

        for j in range(2,13):
            if  (roll1+roll2) == j:
                roll_dict[j] += 1

    for i, result in roll_dict.items():
        print('点数和是{}的次数是{},频率：{}'.format( i , result, result / total_times))

    #  数据可视化
    x = range(1, total_times + 1)
    plt.scatter(x, roll1_list, c= 'red', alpha=0.5)   #alpha表示透明度, c表示颜色
    plt.scatter(x, roll2_list, c='green', alpha=0.5)
    plt.show()


    fp.close()

if __name__ == '__main__':
    main()
