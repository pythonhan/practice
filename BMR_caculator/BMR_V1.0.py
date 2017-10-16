"""
    作者：pythonhan
    功能：BMR计算器
    版本：1.0
    日期：27/09/2017

"""
def main():
    """
    主函数
    """
    # 性别
    gender = '男'

    # 体重
    weight = 70

    # 身高
    height = 172

    # 年龄
    age = 24

    if gender == '男':
        # 男性BMR
        bmr = ( 13.7 * weight ) + ( 5.0 * height ) - ( 6.8 * age) + 66
    elif gender == '女':
        # 女性BMR
        bmr = (9.6 * weight) + (1.8 * height) - (4.7 * age) + 655
    else:
        bmr = -1
    if bmr != -1:
        print('基础代谢率',bmr)
    else:
        print('暂不支持改性别')

if __name__ == '__main__':
    main()