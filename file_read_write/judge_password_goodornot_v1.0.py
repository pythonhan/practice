"""
    作者：pythonhan
    版本：V1.0
    日期：28/09/2017
    功能：判断密码强弱
    用len判断字符串长度，用isnumeric()判断是否只有数字，用isalpha()判断是否只有字母，返回True / False
    str.isnumeric()检测是否只有数字组成
    str.isalpha()检测字符串是否只有字母组成
    str.islower()检测字符串中所有的字母是否都是小写
    str.isupper()检测字符串中所有的字母是否都是大写
    遍历字符串的所有内容
"""
from datetime import datetime

def check_number_exist(password_str):
    """
    判断字符串中是否含有数字
    """
    for c in password_str:
        if c.isnumeric():
            return True
    return False


def check_letter_exist(password_str):
    """
    判断字符串中是否含有字母
    """
    for c in password_str:
        if c.isalpha():
            return True
    return False


def main():
    """
    主函数
    """

    fp = open(r'E:\practice\mytest.txt','a+')
    name = 'judge_password_goodornot_v1.0'
    usage = '判断密码强弱'
    now = datetime.now()
    print('当前操作的程序是：{} \n'.format(name),'',end='',file=fp)
    print('该程序的功能为：{} \n'.format(usage),'',end='',file=fp)
    print('您当前操作时间为：{} \n'.format(now),'',end='',file=fp)
    print('此次运行结果为：\n', '', end='', file=fp)

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
        print('恭喜！密码强度合格\n', '', end='', file=fp)
    else:
        print('密码强度不合格！')
        print('密码强度不合格！\n', '', end='', file=fp)







    fp.close()

if __name__ == '__main__':
    main()
