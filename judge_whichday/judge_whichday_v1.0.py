"""
    作者：pythonhan
    版本：V1.0
    日期：28/09/2017
    功能：输入某年某月某日，判断一个日期属于这一年的第几天
"""
from datetime import datetime
import math

fp = open(r'E:\practice\mytest.txt','a+')



def main():
    """
    主函数
    """
    input_date_str = input('请输入日期（yyyy/mm/dd）: ')
    input_date = datetime.strptime(input_date_str,'%Y/%m/%d')
    year = input_date.year
    month = input_date.month
    day = input_date.day

    # 计算之前月份天数的总和以及当前月份天数
    days_in_month_tup = (31,28,31,30,31,30,31,31,30,31,30,31)
    # days = days_in_month_tup[:month-1]
    days = sum(days_in_month_tup[:month-1]) + day
    # 判断闰年
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        if month > 2:
            days += 1
    print('这是第{}天'.format(days))
print('hello','',end='',file = fp)
fp.close()
if __name__ == '__main__':
    main()