'''
    作者：pythonhan
    日期：27/09/2017
    新增功能：根据输入判断是人民币还是美元
    新增功能：将该函数封装到函数中去
    5.0新增功能：(1)使程序结构化
    (2)简单函数的定义 匿名函数 lambda函数：实验简单的函数定义,能够在一行之内表示的函数
    <函数名> = lambda <参数列表> ： <表达式>
'''

# def convert_currency(im,er):
#     '''
#     汇率兑换
#     '''
#     out = im * er
#     return out

def main():
    '''
    主函数
    '''
    # 汇率,常量要大写
    USD_VS_RMB = 6.77

    currency_str_value = input('请输入带单位的货币金额（退出程序请输入Q）： ')

    # 获取货币单位
    unit = currency_str_value[-3:]

    # 判断是哪种货币并且输出
    if unit == 'CNY':
        exchange_rate = 1 / USD_VS_RMB

    elif unit == 'USD':
        exchange_rate = USD_VS_RMB

    else:
        exchange_rate = -1

    if exchange_rate != -1:
        in_money = eval(currency_str_value[:-3])
    # 使用lambda定义函数名
        convert_currency2 = lambda x: x * exchange_rate
    # # 调用函数
    #     out_money = convert_currency(in_money,exchange_rate)
        out_money = convert_currency2(in_money)
        print('转换后的金额：',out_money)
    else:
        print('目前不支持该种货币！')

if __name__ == '__main__' :
    main()
