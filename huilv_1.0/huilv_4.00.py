'''
    作者：pythonhan
    日期：27/09/2017
    新增功能：根据输入判断是人民币还是美元
    新增功能：将该函数封装到函数中去
'''

def convert_currency(im,er):
    '''
    汇率兑换
    '''
    out = im * er
    return out

# 汇率,常量要大写
USD_VS_RMB = 6.77

currency_str_value = input('请输入带单位的货币金额（退出程序请输入Q）： ')

# 获取货币单位
unit = currency_str_value[-3:]
# 获取金额数值大小

# 判断是哪种货币并且输出
if unit == 'CNY':
    exchange_rate = 1 / USD_VS_RMB

elif unit == 'USD':
    exchange_rate = USD_VS_RMB

else:
    exchange_rate = -1

if exchange_rate != -1:
    in_money = eval(currency_str_value[:-3])
# 调用函数
    out_money = convert_currency(in_money,exchange_rate)
    print('转换后的金额：',out_money)
else:
    print('目前不支持该种货币！')