"""
    作者：pythonhan
    版本：V1.0
    日期：29/09/2017
    功能：模拟投掷骰子，并输出相应的点数
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
"""
from datetime import datetime
import random


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
    name = 'random_v1.00'
    usage = '模拟投掷骰子，并输出相应的点数'
    now = datetime.now()
    print('\n \n 当前操作的程序是：{} \n'.format(name), '', end='', file=fp)
    print('该程序的功能为：{} \n'.format(usage), '', end='', file=fp)
    print('您当前操作时间为：{} \n'.format(now), '', end='', file=fp)
    print('此次运行结果为：\n', '', end='', file=fp)

    total_times = 10000
    # 初始化一个列表[0, 0, 0, 0, 0, 0]
    result_list = [0] * 6


    for i in range(total_times):
        roll = roll_dice()
        for j in range(1,7):
            if  roll == j:
                result_list[j-1] += 1

    for i, result in enumerate(result_list):
        print('点数是{}的次数是{},频率：{}'.format( i + 1, result, result / total_times))



    fp.close()

if __name__ == '__main__':
    main()
