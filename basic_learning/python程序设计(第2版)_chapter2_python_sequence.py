2017年10月23日
python 序列

1. 序列是一块用于存放多个值的连续内存空间。
2. list ,内置可变序列，所有元素放在[],列表元素可修改，增加，删除，除非确实有必要，否则应该尽量从列表尾部进行元素的增加与删除工作，这样会大幅度提高列表处理速度
list中的元素可以同时包含整数，实数，字符串等基本类型，也可以是列表，元组，字典，集合等
['span', 2.9, [1, 2]]
3. list列表对象常用方法：
list.append(x)      #将元素x添加至列表尾部
list.extend(L)      #将列表L中所有元素添加到列表尾部
list.insert(index, x)       #在列表中指定位置index处添加元素x
list.remove(x)              #在列表中删除首次出现的指定元素
list.pop([index])       #删除并返回列表对象指定位置的元素，默认是最后一个元素
list.clear()            #删除列表中所有元素，但是保留列表对象，该方法在python2中没有
list.index(x)           #返回第一个值为x的元素的下表，若不存在，抛出异常
list.count(x)           #返回指定元素x在列表中出现的次数
list.reverse()          #对列表元素进行原地翻转
list.sort()             #列表元素原地排序
list.copy()             #返回列表对象的浅赋值，python2中没有

3. list创建与删除，
