"""
    作者：pythonhan
    日期：09/20/2017
    版本:V10.0
    功能：网络爬虫,用beautifulsoup4解决数据解析问题,获取所有城市的AQI,将获取的CSV指数保存成csv文件,使用pandas进行数据处理
    requests模块
    requests模块是一个简洁且简单的处理HTTP请求的工具
    支持非常丰富的链接访问功能，包括URL获取，HTTP会话，Cookie记录等
    requests网页请求
    get() 对应http的get方式
    post() 对应HTTP的POST方式，用于传递用户数据
    requests对象属性
    status_code HTTP请求的返回状态，200表示链接成功，400表示失败
    text HTTP相应内容的字符串形式，即URL对应的页面内容

    网页解析：
    结构化解析：DOM tree 树形结构，对于任何网页根节点是html,然后是head,title,my title body,div,hi,p,a都是网页元素
    BeautifulSoup库解析网页
    BeautifulSoup 用于解析HTML或者XML
    pip install beautifulsoup4
    import bs4
    步骤：
    1.创建BeautifulSoup对象
    2.查询节点
        find,找到第一个满足条件的节点
        find_all, 找到所有满足条件的节点

    创建对象：
    创建BeautifulSoup对象
    bs = BeautifulSoup(
        url,
        html_parser,指定解析器
        enoding     指定编码格式（确保和网页编码格式一致）
    ）

    查找节点：
    <a href='a.html' class='a_link'> next page</a>
    可按照节点类型、属性或者内容访问
    按照类型查找节点
        bs.find_all('a')
    按照属性查找节点
        bs.find_all('a',href='a.html')
        bs.find_all('a',href='a.html',string='next page')
        bs.find_all('a',class_='a_link')
        注意：是class_
        或者bs.find_all('a',{'class':'a_link'})

    1.首先获取所有的城市列表，以及对应的URL
    2.根据url获取城市的空气质量


    pandas ：一个强大的分析结构化数据的工具集
    基础是NumPy , 提供了高性能矩阵的运算
    应用，数据挖掘，数据分析
        例如学生成绩分析，股票数据分析等
    提供数据清洗功能

    pandas 的数据结构
    Series
    类似于一维数组的对象
    通过list 构建Series
        ser_obj = pd.Series(range(10))
    由数据和索引组成
        索引在左，数据在右
        索引是自动创建的
    获取数据和索引
        ser_obj.index, ser_obj.values
    预览数据
        ser_obj.head(n)  预览前n行数据
        ser_obj.tail(n) 预览后n行数据
    import pandas as pd

    通过索引获取数据
        ser_obj[idx]
    索引与数据的对应关系仍保持在数组运算的结果中
    通过dict构建Series
    name属性
        ser_obj.name, ser_obj.index.name

    对于多维数据 用DataFrame
    类似多维数组/表格数据（例如，excel,R中的data.frame）
    每列数据可以是不同的类型
    索引包括列索引和行索引
    CSV读入的数据一般直接是DateFrame类型
    DateFrame
    通过ndarray构建DataFrame
    通过dict构建 DataFrame
    通过列索引获取列数据（Series类型）
        df_obj[col_idx] 或者 df_obj.col_idx
    增加列数据，类似dict 添加key-value
        df_obj[new_col_idx] = data
    删除列
        del df_obj[col_idx]

    索引操作：
    DataFrame索引
        列索引
            df_obj['label']
        不连续索引
            df_obj[['label1', 'label2']]

    排序：
    sort_index, 索引排序
        对DataFrame操作时注意轴方向
    按值排序
        sort_values(by = 'label')
    Pandas数据清洗
    处理缺失数据
        dropna()    丢弃缺失数据
        fillna()    填充缺失数据
    数据过滤
        df[filter_condition] 依据 filter_condition对数据进行过滤

    Pandas数据可视化
    Pandas提供了内建的绘图功能（基于matplotlib）
    plot(kind, x, y, title, figsize)
    x, y 横纵坐标对应的数据列
    title图像名称
    figsize图像尺寸
    保存图片
    plt.savefig()


"""
#-*-coding:utf-8-*-
import pandas as pd


def main():
    """
    主函数
    """
    aqi_data = pd.read_csv('china_city_aqi.csv')
    # print(aqi_data.head(5))
    print('基本信息：')
    print(aqi_data.info())

    print('数据预览：')
    print(aqi_data.head())
    # print(aqi_data[['City', 'AQI']])
    # 数据清洗
    # 只保留AQI>0的数据
    # filter_condition = aqi_data['AQI'] > 0
    # clean_aqi_data = aqi_data[filter_condition]
    clean_aqi_data = aqi_data[aqi_data['AQI'] > 0]

    # 基本统计
    print('AQI最大值', clean_aqi_data['AQI'].max())
    print('AQI最小值', clean_aqi_data['AQI'].min())
    print('AQI均值', clean_aqi_data['AQI'].mean())

    # top10
    top10_cities = clean_aqi_data.sort_values(by= ['AQI']).head(10)   #升序排列
    # clean_aqi_date.sort_values(by = ['AQI'], ascending= False).tail(10)  #降序排列
    print('空气质量最好的10个城市：')
    print(top10_cities)

    #bottom10
    bottom10_cities = clean_aqi_data.sort_values(by= ['AQI']).tail(10)   #升序排列
    # clean_aqi_date.sort_values(by = ['AQI'], ascending= False).head(10)  #降序排列
    print('空气质量最差的10个城市：')
    print(bottom10_cities)

    #数据保存CSV文件
    # top10_cities.to_csv('top10_aqi.csv', index = False)
    # bottom10_cities.to_csv('bottom10_aqi.csv', index = False)

if __name__ == '__main__':
    main()