'''
    作者：pythonhan
    日期：27/09/2017
'''
# 人民币的输入
rmb_str_value = input('请输入人民币(CNY)金额： ')
# 字符串转换为数字
rmb_value=eval(rmb_str_value)
# 汇率,常量要大写
USD_VS_RMB = 6.77
# 汇率计算
usd_value = (rmb_value / USD_VS_RMB)
print('美元金额是：', usd_value)