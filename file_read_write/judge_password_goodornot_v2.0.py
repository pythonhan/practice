"""
    作者：pythonhan
    版本：V2.0
    日期：28/09/2017
    功能：判断密码强弱
    2.0新增功能：循环的终止
    用len判断字符串长度，用isnumeric()判断是否只有数字，用isalpha()判断是否只有字母，返回True / False
    str.isnumeric()检测是否只有数字组成
    str.isalpha()检测字符串是否只有字母组成
    str.islower()检测字符串中所有的字母是否都是小写
    str.isupper()检测字符串中所有的字母是否都是大写
    遍历字符串的所有内容
    break 终止整个循环，程序结束
    continue 只终止本次循环，接着去判断，而不终止整个循环的执行
    for i in range(100):
        if i % 2 == 0:
            break（输入0时程序结束）/continue（输入0退出，输入1输出，输入2退出……）
        print(i)
"""
from datetime import datetime

def check_number_exist(password_str):
    """
    判断字符串中是否含有数字
    """
    has_number = False
    for c in password_str:
        if c.isnumeric():
            has_number = True
            break
    return has_number


def check_letter_exist(password_str):
    """
    判断字符串中是否含有字母
    """
    has_letter = False
    for c in password_str:
        if c.isalpha():
            has_letter = True
            break
    return has_letter


def main():
    """
    主函数
    """

    fp = open(r'E:\practice\mytest.txt','a+')
    name = 'judge_password_goodornot_v2.0'
    usage = '判断密码强弱， 2.0新增功能：循环的终止'
    now = datetime.now()
    print('\n \n 当前操作的程序是：{} \n'.format(name),'',end='',file=fp)
    print('该程序的功能为：{} \n'.format(usage),'',end='',file=fp)
    print('您当前操作时间为：{} \n'.format(now),'',end='',file=fp)
    print('此次运行结果为：\n', '', end='', file=fp)

    try_times = 5

    while try_times > 0:
        password = input('请输入密码：')

        # 密码强度
        strength_level = 0

        # 规则1：密码长度大于8
        if len(password) >= 8:
            strength_level += 1
        else:
            print('密码长度要求至少8位！')
            print('密码长度要求至少8位！\n','',end='',file=fp)

        # 规则2：判断是否有数字存在
        if check_number_exist(password) :
            strength_level += 1
        else:
            print('密码要求包含数字!')
            print('密码要求包含数字!\n', '', end='', file=fp)

        # 规则3：判断是否有字母存在
        if check_letter_exist(password):
            strength_level += 1
        else:
            print('密码要求包含字母!')
            print('密码要求包含字母!\n', '', end='', file=fp)

        if strength_level == 3:
            print('恭喜！密码强度合格')
            break
            print('恭喜！密码强度合格\n', '', end='', file=fp)
        else:
            print('密码强度不合格！')
            try_times -= 1
            print('密码强度不合格！\n', '', end='', file=fp)

    if try_times <= 0:
        print('尝试次数过多，密码设置失败！')
        print('尝试次数过多，密码设置失败！\n', '', end='', file=fp)





    fp.close()

if __name__ == '__main__':
    main()
