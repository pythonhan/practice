"""
    作者：pythonhan
    日期：09/20/2017
    版本:V5.0
    功能：网络爬虫
    requests模块
    requests模块是一个简洁且简单的处理HTTP请求的工具
    支持非常丰富的链接访问功能，包括URL获取，HTTP会话，Cookie记录等
    requests网页请求
    get() 对应http的get方式
    post() 对应HTTP的POST方式，用于传递用户数据
    requests对象属性
    status_code HTTP请求的返回状态，200表示链接成功，400表示失败
    text HTTP相应内容的字符串形式，即URL对应的页面内容
"""
import requests

def get_html_text(url):
    """
        返回url的文本
    """
    r = requests.get(url,timeout=30)
    # print(r.status_code)
    return r.text


def main():
    """
    主函数
    """
    city_pinyin = input('请输入城市拼音：')
    url = 'http://pm25.in/' + city_pinyin
    url_text = get_html_text(url)
    # 要取到上面包括空格的位置
    aqi_div = '''<div class="span12 data">
        <div class="span1">
          <div class="value">
            '''
    index = url_text.find(aqi_div)
    begin_index = index + len(aqi_div)
    end_index = begin_index + 2
    aqi_val = url_text[begin_index:end_index]
    print('空气质量为：{}'.format(aqi_val))

if __name__ == '__main__':
    main()