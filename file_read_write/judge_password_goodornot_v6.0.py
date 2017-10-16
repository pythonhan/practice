"""
    作者：pythonhan
    版本：V6.0
    日期：28/09/2017
    功能：判断密码强弱
    2.0新增功能：循环的终止
    3.0新增功能：将密码和强度存到文本中
    4.0新增功能：读取之前存储的密码
    5.0新增功能; 定义一个password工具类
    6.0新增功能：将文件操作封装到一个类中
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

    面向对象： 对象  属性  行为

    类：某种类型集合的描述    属性： 类本身的一些特性  方法：类所能实现的行为，对应的就是函数
    类的定义：
    class ClassName
    __init__(self)构造函数：初始化对象的各种属性
    self代表类的实例
"""
from datetime import datetime

class PasswordTool:
    """
    密码工具类
    """
    # 先定义静态属性
    def __init__(self, password):
        self.password = password
        self.strength_level = 0

    # 再定义类的方法，函数
    def process_password(self):
        # 规则1：密码长度大于8
        if len(self.password) >= 8:
            self.strength_level += 1
        else:
            print('密码长度要求至少8位！')
            print('密码长度要求至少8位！\n', '', end='', file=fp)

        # 规则2：判断是否有数字存在
        if self.check_number_exist():
            self.strength_level += 1
        else:
            print('密码要求包含数字!')
            print('密码要求包含数字!\n', '', end='', file=fp)

        # 规则3：判断是否有字母存在
        if self.check_letter_exist():
            self.strength_level += 1
        else:
            print('密码要求包含字母!')
            print('密码要求包含字母!\n', '', end='', file=fp)



    def check_number_exist(self):
        """
        判断字符串中是否含有数字
        """
        has_number = False
        for c in self.password:
            if c.isnumeric():
                has_number = True
                break
        return has_number


    def check_letter_exist(self):
        """
        判断字符串中是否含有字母
        """
        has_letter = False
        for c in self.password:
            if c.isalpha():
                has_letter = True
                break
        return has_letter

class FileTool:
    """
    文件工具类
    """
    def __init__(self,filepath):
        self.filepath = filepath

    def write_to_file(self, line):
        f = open(self.filepath, 'a')
        f.write(line)
        f.close()

    def read_from_file(self):
        f = open(self.filepath, 'r')
        lines = f.readlines()
        f.close()
        return lines
def main():
    """
    主函数
    """

    fp = open(r'E:\practice\mytest.txt','a+')
    name = 'judge_password_goodornot_v5.0'
    usage = '判断密码强弱， 2.0新增功能：循环的终止，3.0新增功能：将密码和强度存到文本中，4.0新增功能：读取之前存储的密码，5.0新增功能; 面向对象编程，封装成一个对象，6.0新增功能：将文件操作封装到一个类中'
    now = datetime.now()
    print('\n \n 当前操作的程序是：{} \n'.format(name),'',end='',file=fp)
    print('该程序的功能为：{} \n'.format(usage),'',end='',file=fp)
    print('您当前操作时间为：{} \n'.format(now),'',end='',file=fp)
    print('此次运行结果为：\n', '', end='', file=fp)

    try_times = 5
    filepath = 'password_6.0.txt'
    file_tool = FileTool(filepath)
    while try_times > 0:
        password = input('请输入密码：')
        # 实例化密码工具对象
        password_tool = PasswordTool(password)
        password_tool.process_password()

        line = '密码是：{},强度是：{}\n'.format(password_tool.password, password_tool.strength_level)
        file_tool.write_to_file(line)
        if password_tool.strength_level == 3:
            print('恭喜！密码强度合格')
            print('恭喜！密码强度合格\n', '', end='', file=fp)
            break

        else:
            print('密码强度不合格！')
            try_times -= 1
            print('密码强度不合格！\n', '', end='', file=fp)

        # 实例化文件工具对象


    if try_times <= 0:
        print('尝试次数过多，密码设置失败！')
        print('尝试次数过多，密码设置失败！\n', '', end='', file=fp)

    file_tool.read_from_file()
    fp.close()

if __name__ == '__main__':
    main()
