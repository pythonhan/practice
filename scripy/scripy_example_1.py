"""
    作者：pythonhan
    日期：09/10/2017
    版本：
    功能：
    笔记：
    1.互联网，爬虫和图书馆：
        传统的数据资料获取成本极高，
        软件时代：数据传输成为信息搜集的瓶颈
        互联网：开放标准、信息交流渠道的演变
    2.爬虫的典型应用
        Yahoo，google、百度:搜索引擎
        今日头条：新闻聚合
        大数据： 数据采集
        间谍软件：情报搜集
        wikiwand： 内容的二次加工

    3.爬虫的基础知识
        静态网页的爬虫就是对由url组成的数进行遍历
    4.完成一个通用爬虫
        设置种子站点、宽度及深度
        一个已下载的队列来记录所有已经完成下载的url
        实现一个函数，取得当前url的内容以及所有的外链
        递归调用这个函数，来遍历网站
        错误记录
    5.网页
        静态网页
        动态网页
        Web Service(有请求之后直接返回结果)用web view直接来渲染一些内容即可，套用本地模板直接呈现，例如地图位置信息
    6.HTML规范
        Html, html都是公开的，而移动端APP标准都是自己定义的，所以爬虫回来也看不懂，是因为是私有方式来加密的
        Javascript
        CSS
    7.HTML
        tag: <a> <tr> <p>
        Class: class='home-price'
        id:id = price-frame
        DOM

    examples:
    1.获取所有汽车型号
        从哪里获得汽车信息
        评估数据与我们雪球的匹配度
        评估复杂度
        动态还是静态

"""
import urllib2
import json
from bs4 import BeautifulSoup


def get_cars(url_format):
    pass



def main():
    """
        主函数
    """
    url_format = "http://www.autohome.com.cn/grade/carhtml/{}.html"
    request_header = {
    'host': "www.autohome.com.cn",
    'connection': "keep-alive",
    'accept': "*/*",
    'x-requested-with': "XMLHttpRequest",
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36",
    'referer': "http://www.autohome.com.cn/car/",
    'accept-encoding': "gzip, deflate",
    'accept-language': "zh-CN,zh;q=0.8",
    'cookie': "ASP.NET_SessionId=vhdz1rqpkryastsdli2q5smo; UM_distinctid=15f03f70354111-01b7f1b747276f-63151074-100200-15f03f7035534f; fvlid=1507600037823NyOfBne5C8; sessionip=60.247.46.227; sessionid=AD225F4B-8DD5-44CC-A89C-01C62614E41C%7C%7C2017-10-10+09%3A49%3A53.152%7C%7Cwww.baidu.com; ahpau=1; sessionuid=AD225F4B-8DD5-44CC-A89C-01C62614E41C%7C%7C2017-10-10+09%3A49%3A53.152%7C%7Cwww.baidu.com; pvidlist=28e98801-2fc1-458b-9b20-9d06d6991c3a13:106522:153996:0:1:857863; ahpvno=6; CNZZDATA1262640694=47793919-1507597331-null%7C1507597331; ref=www.baidu.com%7C0%7C0%7C0%7C2017-10-10+10%3A05%3A13.356%7C2017-10-10+09%3A49%3A53.152; sessionvid=F076F459-51BA-49A6-9ACE-B6891A41ABBD; area=110199; ahrlid=1507600958116M5jIKEzWda-1507602061076",
    'cache-control': "no-cache",
    'postman-token': "e7bd377a-f910-651a-66ba-c5b2aa22f506"
    }

    html_doc = ''
    start_char = 'A'

    for i in range(ord('A'), ord('Z')):  # ord是把字符转成数字
        req = urllib2.Request(url_format.format(chr(i)), headers = request_header)
        response = urllib2.urlopen(req)
        page = response.read()
        html_doc += page

        fo = open('autohome.html', 'wb+')
        fo.write(html_doc)
        fo.close
if __name__ == '__main__':
    main()