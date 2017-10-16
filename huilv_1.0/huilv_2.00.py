'''
    作者：pythonhan
    日期：27/09/2017
    新增功能：根据输入判断是人民币还是美元
'''
# 汇率,常量要大写
USD_VS_RMB = 6.77

# 带单位的货币输入，为字符串
currency_str_value = input('请输入带单位的货币金额： ')
# 获取货币单位
unit = currency_str_value[-3:]
# 获取金额数值大小
value = currency_str_value[:-3]
# 判断是哪种货币并且输出
if unit == 'CNY':
    rmb_value = eval(value)
    print('您输入的是人民币金额为：',rmb_value)
    print('转换成美元后的金额大小为： ', rmb_value / USD_VS_RMB)
elif unit == 'USD':
    usd_value = eval(value)
    print('您输入的是美元金额为： ',usd_value)
    print('转换成人民币后的金额大小为： ', usd_value * USD_VS_RMB)
else:
    print('该程序目前版本尚不支持该种货币！')
# # 字符串转换为数字
# rmb_value=eval(rmb_str_value)
#
# # 汇率计算
# usd_value = (rmb_value / USD_VS_RMB)
# print('美元金额是：', usd_value)