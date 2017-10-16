#! usr/bin/python #coding=utf-8
'''
    作者：pythonhan
    功能：52周存钱挑战
    版本：V6.0
    日期：28/09/2017
    新增功能：保存，将每周存的钱数放入列表中，再取出查看等
    4.0新增功能：使用for循环
    5.0新增功能：灵活设置每周存款数，增加的存款数等
    6.0新增功能：根据用户输入的日期，判断是第几周，输出相应的金额
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

    datetime库
    datetime.datetime.now()当前时间
    如果now = datetime.datetime.now()
    now.year可以输出年
    now.month
    now.day
    now.isocalendar()   （2017,31,6）输出当前日期所在周数，星期
    datetime.datetime.strptime('2017/08/05',format('%Y/%m/%d'))  y表示两位数的年份
    datetime.datetime.strptime('2017/08/05','%Y/%m/%d')
    字符串转换成datetime.  datetime.datetime.strptime()，解析当前字符串
    datetime转换成字符转， strftime 格式化datetime为字符串显示
    isocalendar()返回年，周数，及周几
    datetime.datetime.strftime(now, '%d/%m/$Y') 按照给定的顺序来转换
'''
import math
import datetime
saving = 0
def save_money_in_n_weeks(money_per_week,increase_money,total_week):
    """
    计算n周内的存款金额
    """
    global saving   # 账户累计,声明为全局变量，在所有函数中都能使用，不声明不能在函数内使用
    fp = open(r'E:\practice\mytest.txt', 'a+')
    money_list = []  # 记录每周存款数的列表
    saved_money_list = [] # 记录账户累计
    for i in range(total_week):
        # 存钱操作
        # saving += money_per_week
        money_list.append(money_per_week)
        saving = math.fsum(money_list)
        saved_money_list.append(saving)
        # 输出信息
        print('第{}周， 存入{}元钱， 账户累计{}元 \n'.format(i + 1, money_per_week, saving), '', end='', file=fp)
        # 更新下一周存钱金额
        money_per_week += increase_money
    fp.close()
    return saved_money_list

def main():
    '''
    主函数
    '''
    money_per_week = float(input('请输入每周存入的金额：')) #每周存入的金额
    increase_money = float(input('请输入每周的递增金额： ')) #递增的金额
    total_week = int(input('请输入总共的周数'))    #总共周数
    saved_money_list = save_money_in_n_weeks(money_per_week,increase_money,total_week)
    input_date_str = input('请输入日期（yyyy/mm/dd）：')
    input_date = datetime.datetime.strptime(input_date_str,'%Y/%m/%d')
    week_num =input_date.isocalendar()[1]
    print('第{}周的存款金额是{}元'.format(week_num,saved_money_list[week_num-1]))
if __name__ == '__main__':
    main()