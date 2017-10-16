#! usr/bin/python #coding=utf-8
'''
    作者：pythonhan
    功能：52周存钱挑战
    版本：V5.0
    日期：27/09/2017
    新增功能：保存，将每周存的钱数放入列表中，再取出查看等
    4.0新增功能：使用for循环
    5.0新增功能：灵活设置每周存款数，增加的存款数等
    列表：有序的元素集合，可以通过索引访问某个元素，list，也可以区间访问，列表中每个元素可以不同
    相加：合并或者连接两个list
    list1+list2
    list * n 重复
    len(list) 查看列表长度
    x in list 查看某个元素是否在该列表中，返回值为判断语句的返回值Ture or False
    list.append() 将某个元素添加到数组的末尾
    list.sort()对列表重新重新排序
    list.reverse()对数组进行逆序输出
    list.index(x)查看元素的位置
    list.insert(i,x)在i个位置添加x
    list.count(x)返回元素在列表中的个数
    list.remove(x)删除元素
    list.pop(i)删除某个位置的元素
    math库
    math.fsum(list)对集合内的元素求和
    math.pi 圆周率
    math.ceil(x) 对一个数向上取整数
    math.floor(x)向下取整
    math.pow(x,y)x的y次方
    math.sqrt(x) 开根号
    for 循环 直接记录数据
    for x in list:每一次循环x拿到的是列表中的内容，直到把列表遍历完，
        无需指定结束条件，与while的区别是次数是固定的，for为遍历序列长度的循环
        while为无限循环
    指定循环次数：用range
    for i in range(10)  从0-9
    for i in range(10,20) 从10-19
    list(range())变成list
'''
import math

saving = 0
def save_money_in_n_weeks(money_per_week,increase_money,total_week):
    """
    计算n周内的存款金额
    """
    global saving   # 账户累计,声明为全局变量，在所有函数中都能使用，不声明不能在函数内使用
    fp = open(r'E:\practice\mytest.txt', 'a+')
    money_list = []  # 记录每周存款数的列表
    for i in range(total_week):
        # 存钱操作
        # saving += money_per_week
        money_list.append(money_per_week)
        saving = math.fsum(money_list)
        # 输出信息
        print('第{}周， 存入{}元钱， 账户累计{}元'.format(i + 1, money_per_week, saving))
        print('第{}周， 存入{}元钱， 账户累计{}元 \n'.format(i + 1, money_per_week, saving), '', end='', file=fp)
        # 更新下一周存钱金额
        money_per_week += increase_money
    fp.close()
    print('函数内的saving: ',saving)   #输出的是总的saving
    return saving

def main():
    '''
    主函数
    '''
    money_per_week = float(input('请输入每周存入的金额：')) #每周存入的金额
    increase_money = float(input('请输入每周的递增金额： ')) #递增的金额
    total_week = int(input('请输入总共的周数'))    #总共周数
    save_money_in_n_weeks(money_per_week,increase_money,total_week)
    print('函数外的saving:',saving)  #输出的是函数外的saving=0
if __name__ == '__main__':
    main()