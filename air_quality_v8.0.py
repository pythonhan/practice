"""
    作者：pythonhan
    日期：09/20/2017
    版本:V7.0
    功能：网络爬虫,用beautifulsoup4解决数据解析问题,获取所有城市的AQI,将获取的CSV指数保存成csv文件
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

"""
import requests
from bs4 import BeautifulSoup
import csv

def get_city_aqi(city_pinyin):
    """
        获取城市aqi
    """
    url = 'http://pm25.in/' + city_pinyin
    r = requests.get(url, timeout=200)
    soup = BeautifulSoup(r.text, 'lxml')
    div_list = soup.find_all('div',{'class':'span1'})

    city_aqi = []
    for i in range(8):
        div_content = div_list[i]
        caption = div_content.find('div',{'class':'caption'}).text.strip()
        value = div_content.find('div',{'class':'value'}).text.strip()

        city_aqi.append(value)
    return city_aqi

def get_all_cities():
    """
        获取所有的城市
    """
    url = 'http://pm25.in/'
    r = requests.get(url, timeout=30)
    soup = BeautifulSoup(r.text, 'lxml')

    city_div = soup.find_all('div', {'class':'bottom'})[1]

    city_link_list = city_div.find_all('a')
    city_list = []

    for city_link in city_link_list:
        city_name = city_link.text
        city_pinyin = city_link['href'][1:]
        city_list.append((city_name,city_pinyin))
    return city_list

def main():
    """
    主函数
    """
    city_list = get_all_cities()
    # for city in city_list:
    #     city_name = city[0]
    #     city_pinyin = city[1]
    #     city_aqi = get_city_aqi(city_pinyin)
    #     print((city_name,city_aqi))
    header = ['City', 'AQI', 'PM2.5/1h', 'PM10/1h', 'CO/1h', 'NO2/1h', 'O3/1h', 'O3/8h', 'SO2/1h']

    with open('china_city_aqi.csv','w', encoding='utf-8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for i,city in enumerate(city_list):
            if (i + 1) % 10 == 0:
                print('已处理{}条记录（共{}条记录）'.format(i + 1, len(city_list)))

            city_name = city[0]
            city_pinyin = city[1]
            city_aqi = get_city_aqi(city_pinyin)
            row = [city_name] + city_aqi
            writer.writerow(row)

if __name__ == '__main__':
    main()