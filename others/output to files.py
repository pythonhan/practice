def main1():
    fp = open(r'E:\practice\mytest.txt','a+')
    for i in range(10, 20):
        print(i, '', end='',file=fp)
    fp.close()
    print('finish')
main1()