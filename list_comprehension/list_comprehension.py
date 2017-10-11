"""
    作者：pythonhan
    时间：11/10/2017
    学习笔记：
    List Comprehension :python 进阶：列表推导式
        快速简洁的构造一个新列表
    基本语法：
    [expression for item in list if conditional]

    result = []
    for item in list:
        if conditonal:
            result.append(expression)
    用seaborn 作图比 pandas要好
    Kaggle案例 ：数据挖掘常用， 是一个平台，有公开的竞赛，公开的数据集
    Jupyter 代码展示
    约定俗成的简称：
    import pandas as pd
    import seaborn as sns
    import numpy as np
    import matplotlib.pyplot as plt

    listing_data = pd.read_csv('./文件路径.csv', usecols = ['property_type', 'room_type', 'accommodates', 'bedrooms', 'price', '标签'])
    listing_data.head()   #预览

    price_data_list = list_data['price'].tolist()   #tolist函数,拿出其中一列数据

    price_list = [float(item.replace(',', '')[1:]) for item in price_data_list]  #将西方数字里的,替换掉,用切片操作去掉单位符
    listing_data['price'] = price_list      #将处理后的数据赋值给price列
    listing_data.head()

    plt.figure(figsize = (12, 6))
    sns.boxplot(x = 'property_type', y = 'price', data = listing_data)
    xt = plt.xticks(rotation = 90)

    sns.factorplot('accommodates', 'price', data = listing_data, color = 'm', \estimator = np.median, size = 4.5, aspect = 1.35)
    xt = plt.xticks(rotation = 90)


"""

def main():
    """
        主函数
    """
    tool_list = ['r', "python", 'scale', 'matlab', 'sas', 'spss']
    answer1 = [x.upper() for x in tool_list if len(x) >= 3]
    print('answer1 is :{}'.format(answer1))

    int_list = range(100)
    answer2 = [x**2 for x in int_list if x >= 30 and x <= 40]
    print('answer2 is :{}'.format(answer2))

if __name__ == '__main__':
    main()