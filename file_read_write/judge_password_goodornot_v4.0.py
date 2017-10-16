"""
    作者：pythonhan
    版本：V3.0
    日期：28/09/2017
    功能：判断密码强弱
    2.0新增功能：循环的终止
    3.0新增功能：将密码和强度存到文本中
    4.0新增功能：读取之前存储的密码
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

    打开文件-操作文件-关闭文件
    1.打开文件：建立文件和程序的关联
    open(filename,mode)
    filename:文件名（包括路径）
    mode:打开模式，有以下模式
    r 只读文件，文件不存在报错
    w 只写文件，文件不存在自动创建
    a 在文件末尾附加
    r+ 读写
    2.写入操作；
    write():将文本数据写入文件中
    writelines(str):将字符串列表写入文件中
    读操作：
    read(): 返回值为包含整个文件内容的一个字符串
    readline():返回值为文件下一行内容的字符串
    readlines():返回值为整个文件内容的列表每项是一行，换行符结束
    3.关闭文件：
    file.close()
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
    name = 'judge_password_goodornot_v4.0'
    usage = '判断密码强弱， 2.0新增功能：循环的终止，3.0新增功能：将密码和强度存到文本中，4.0新增功能：读取之前存储的密码'
    now = datetime.now()
    print('\n \n 当前操作的程序是：{} \n'.format(name),'',end='',file=fp)
    print('该程序的功能为：{} \n'.format(usage),'',end='',file=fp)
    print('您当前操作时间为：{} \n'.format(now),'',end='',file=fp)
    print('此次运行结果为：\n', '', end='', file=fp)

    # try_times = 5
    #
    # while try_times > 0:
    #     password = input('请输入密码：')
    #
    #     # 密码强度
    #     strength_level = 0
    #
    #     # 规则1：密码长度大于8
    #     if len(password) >= 8:
    #         strength_level += 1
    #     else:
    #         print('密码长度要求至少8位！')
    #         print('密码长度要求至少8位！\n','',end='',file=fp)
    #
    #     # 规则2：判断是否有数字存在
    #     if check_number_exist(password) :
    #         strength_level += 1
    #     else:
    #         print('密码要求包含数字!')
    #         print('密码要求包含数字!\n', '', end='', file=fp)
    #
    #     # 规则3：判断是否有字母存在
    #     if check_letter_exist(password):
    #         strength_level += 1
    #     else:
    #         print('密码要求包含字母!')
    #         print('密码要求包含字母!\n', '', end='', file=fp)
    #
    #     if strength_level == 3:
    #         print('恭喜！密码强度合格')
    #         f = open('password_3.0.txt', 'a+')  # 不会把之前存入的内容冲掉，在文末继续添加
    #         f.write('密码是：{},强度是：{}\n'.format(password,strength_level))
    #         f.close()
    #         print('恭喜！密码强度合格\n', '', end='', file=fp)
    #         break
    #
    #     else:
    #         print('密码强度不合格！')
    #         try_times -= 1
    #         print('密码强度不合格！\n', '', end='', file=fp)
    #     f = open('password_3.0.txt', 'a+')  # 不会把之前存入的内容冲掉，在文末继续添加
    #     f.write(password + '\n')
    #     f.close()
    # if try_times <= 0:
    #     print('尝试次数过多，密码设置失败！')
    #     print('尝试次数过多，密码设置失败！\n', '', end='', file=fp)


    f = open('password_3.0.txt','r')
    # 1.read()
    # content = f.read()
    # print(content)

    # 2.readline()
    # content = f.readline() #只读取一行

    # 3.readlines()
    # lines = f.readlines() #返回为列表
    for line in f.readlines():
        print('read:{}'.format(line))
    f.close()

    fp.close()

if __name__ == '__main__':
    main()
