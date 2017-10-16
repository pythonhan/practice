"""
    作者：pythonhan
    版本：V2.00
    日期：09/10/2017
    功能：空气质量计算
    介绍csv文件和JSON数据文件
    将 JSON数据文件转换成CSV文件
    CSV是一种通用的，相对简单的文件格式，在商业和科学领域上广泛使用
    规则：一行为单位，每行表示一条记录，以英文逗号分割每列数据（若数据为空，逗号也要保留），列名通常放置在文件的第一行

    import csv
    csv.writerow(list) 将列表中的元素写入文件的一行中

    读取已经获取的JSON数据文件
    并将AQI前5的数据输出到另外一个文件中
    JSON 是一种轻量级数据交换格式，其实也是一种文本数据
    可以对复杂数据进行表达和储存，易于阅读和理解
    规则：数据保存在键值对中，键值对之间由逗号分隔， 花括号用于保存键值对数据组成的对象，方括号用于保存键值对数据组成的数组（多个对象）
    采用对象、数组方式直起来的键值对可以表示任何结构的数据
    JSON格式是互联网上主要使用的复杂数据格式之一

    JSON库是处理JSON格式的PYTHON标准库
    两个过程:编码和解码
    编码：将python数据里诶性转换成json格式的过程
    解码：反过来
    dumps() 将python 数据类型转换成JSON格式
    loads() 将json格式字符串转换成PYTHON数据类型
    dump() 与dumps()功能一致，输出到文件
    load() 与loads()功能一致， 从文件读入

    列表排序：
    list.sort(func)
    func 指定了排序的方法
    func 可以通过lambda函数实现

"""
import json
import csv

def process_json_file(filepath):
    """
        解码json文件
    """
    f = open(filepath, mode='r', encoding='utf-8')
    city_list = json.load(f)
    return city_list

def main():
    """
        主函数
    """

    filepath = input('请输入json文件名称：')
    city_list = process_json_file(filepath)
    city_list.sort(key = lambda city: city['aqi'])

    lines = []
    # 列名字
    lines.append(list(city_list[0].keys()))
    for city in city_list:
        lines.append(list(city.values()))

    f = open('aqi.csv', 'w', encoding='utf-8', newline='')
    writer = csv.writer(f)
    for line in lines:
        writer.writerow(line)
    f.close()


    f.close

if __name__ == '__main__':
    main()