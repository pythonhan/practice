import os
import sys
import datetime

head='#'+'-'*20+'\n'+\
    '#Function description:\n'+\
    '#'+'-'*20+'\n'+\
    '#Author:Pythonhan\n'+\
    '#QQ:350748650\n'+\
    'Email:16120187@bjtu.edu.cn\n'+\
    '#'+'-'*20+'\n'
desFile=sys.argv[1]  #目标文件名
if os.path.exists(desFile) or not desFile.endswith('.py'):
    print('%s already exist or is not a Python code file:!' % desFile)
    sys.exit()
fp=open(desFile,'w')
today=str(datetime.date.today())
fp.write('#-*-coding:utf-8-*-\n')
fp.write('#Filename:'+desFile+'\n')
fp.write(head)
fp.write('#Data:'+today+'\n')
fp.write('#'+'-'*20+'\n')
fp.close()