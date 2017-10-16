"""
    作者：pythonhan
    版本：V4.0
    日期：28/09/2017
    功能：输入某年某月某日，判断一个日期属于这一年的第几天
    2.0新增功能：用列表list来替代元组tuple
    3.0新增功能：将月份划分为不同的集合
    4.0新增功能：把天数和月份放在一起，字典的方式，是一个键值对的组合，dict()输出的为{}和set()输出都是{}，字典类型通过映射查找数据项，字典是无顺序的key-value，dict['key']=value
    {'a':12, 'b':15}
    d['a']
    删除
    del d['a']
    检查某个key是否在字典中
    'a' in dict
    集合set()函数，集合中的元素是不可重复的，没有索引和位置的概念，返回结果是一个无重复且排序任意的集合，表示去重，集合关系等
    set(list)变成{list去重}
    集合操作，s - t 或者s.different(t) 返回在s中不在t中的集合
    s & t 或者 s.intersection(t)  交集
    s | t 或者 s.union(t)  返回集合s和t中的所有元素
    s ^ t 或者 s.symmetric_difference(t)  返回s和t中的元素，但不包括交集中的元素
     if d 是一个dict
     for key in d.keys():   遍历所有的key
        print(key)
    for value in d.values(): 遍历所有的value
        print(value)
    for item in d.items():  遍历所有的item
        print(item)

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


    ## 包含30天的月份集合
    # _30_days_month_set = {4, 6, 9, 11}
    # _31_days_month_set = {1, 3, 5, 7, 8, 10, 12}
    # 月份天数字典
    month_day_dict = {1:31,
                      2:28,
                      3:31,
                      4:30,
                      5:31,
                      6:30,
                      7:31,
                      8:31,
                      9:30,
                      10:31,
                      11:30,
                      12:31}
    # 天数月份字典
    # day_month_dict = {30: {4,6,9,11},
    #                   31: {1, 3, 5, 7, 8, 10, 12}}

    # 初始化值
    days = 0
    days += day

    for i in range( 1, month):
        days += month_day_dict[i]

    if is_leap_year(year) and month > 2:
        days += 1

    # # 计算之前月份天数的总和以及当前月份天数
    # days_in_month_list = [31,28,31,30,31,30,31,31,30,31,30,31]
    # # days = days_in_month_tup[:month-1]
    # if is_leap_year(year):
    #     days_in_month_list[1] = 29
    # days = sum(days_in_month_list[:month-1]) + day

    print('这是{}年的第{}天'.format(year,days))
    now = datetime.now()
    print('当前操作时间是：{} \n'.format(now), '', end='', file=fp)
    print('您输入的日期是：{} \n'.format(input_date), '', end='', file=fp)
    print('这是{}年的第{}天 \n'.format(year, days), '', end='', file=fp)
    fp.close()


if __name__ == '__main__':
    main()
