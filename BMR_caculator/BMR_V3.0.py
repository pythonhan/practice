"""
    作者：pythonhan
    功能：BMR计算器
    版本：3.0
    日期：27/09/2017
    2.0新增功能：根据用户的输入，得出BMR值
    3.0新增功能：用户可以一行输入所有信息，带单位的信息输出
    str.split()空格中写以什么分割，分割字符串
    print('{0}KG,{1}厘米,{0}KG)'.format(40,175)
    可以自己指定位置信息，不指定为默认顺序
"""
def main():
    """
    主函数
    """
    y_or_n = input('是否退出程序（y/n）?  ')

    while y_or_n != 'y':
        # # 性别
        # gender = input('性别：')
        # # 体重
        # weight = float(input('体重（kg）：'))
        # # 身高
        # height = float(input('身高（cm）：'))
        # # 年龄
        # age = int(input('年龄：'))
        print('请输入一下信息：用空格分割\n')
        input_str = input('性别 体重（kg） 身高（cm） 年龄： ')
        str_list = input_str.split(' ')
        gender = str_list[0]
        weight = float(str_list[1])
        height = float(str_list[2])
        age = int(str_list[3])

        if gender == '男':
            # 男性BMR
            bmr = ( 13.7 * weight ) + ( 5.0 * height ) - ( 6.8 * age) + 66
        elif gender == '女':
            # 女性BMR
            bmr = (9.6 * weight) + (1.8 * height) - (4.7 * age) + 655
        else:
            bmr = -1
        if bmr != -1:
            print('您的性别：{}， 体重：{}公斤， 身高：{}厘米， 年龄：{}岁'.format(gender,weight,height,age))
            print('您的基础代谢率：{} 大卡'.format(round(bmr,2)))
        else:
            print('暂不支持改性别')
        print()
# 参数为空时输出空行
        y_or_n = input('是否退出程序（y/n）?')
    else:
        print('程序退出!')

if __name__ == '__main__':
    main()