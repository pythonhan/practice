"""
    作者：pythonhan
    版本：V3.0
    日期：28/09/2017
    功能：输入某年某月某日，判断一个日期属于这一年的第几天
    2.0新增功能：用列表list来替代元组tuple
    3.0新增功能：将月份划分为不同的集合
    集合set()函数，集合中的元素是不可重复的，没有索引和位置的概念，返回结果是一个无重复且排序任意的集合，表示去重，集合关系等
    set(list)变成{list去重}
    集合操作，s - t 或者s.different(t) 返回在s中不在t中的集合
    s & t 或者 s.intersection(t)  交集
    s | t 或者 s.union(t)  返回集合s和t中的所有元素
    s ^ t 或者 s.symmetric_difference(t)  返回s和t中的元素，但不包括交集中的元素

"""
from datetime import datetime
import math



def is_leap_year(year):
    """
        判断是否是闰年
        是返回True
        否返回False
    """
    is_leap = False

    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        is_leap = True
    return is_leap


def main():
    """
    主函数
    """
    fp = open(r'E:\practice\mytest.txt', 'a+')
    input_date_str = input('请输入日期（yyyy/mm/dd）: ')
    input_date = datetime.strptime(input_date_str,'%Y/%m/%d')
    year = input_date.year
    month = input_date.month
    day = input_date.day


    # 包含30天的月份集合
    _30_days_month_set = {4, 6, 9, 11}
    _31_days_month_set = {1, 3, 5, 7, 8, 10, 12}

    # 初始化值
    days = 0
    days += day

    for i in range( 1, month):
        if i in _30_days_month_set:
            days += 30
        elif i in _31_days_month_set:
            days += 31
        else:
            days += 28
    if is_leap_year(year) and month > 2:
        days += 1

    # # 计算之前月份天数的总和以及当前月份天数
    # days_in_month_list = [31,28,31,30,31,30,31,31,30,31,30,31]
    # # days = days_in_month_tup[:month-1]
    # if is_leap_year(year):
    #     days_in_month_list[1] = 29
    # days = sum(days_in_month_list[:month-1]) + day

    print('这是{}年的第{}天'.format(year,days))
    print('您输入的日期是：{} \n'.format(input_date), '', end='', file=fp)
    print('这是{}年的第{}天 \n'.format(year, days), '', end='', file=fp)
    fp.close()


if __name__ == '__main__':
    main()
