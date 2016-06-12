#######################################################################
# Python2_02: Data Types in Python / 基本数据类型
# 本文分为以下几部分：
# 0. 基础
#     0-0. 帮助文档的语法规范
#     0-1. sorted() 函数举例
#     0-2. 其他注意点
# 1. 类型和内存地址
# 2. 数学计算
# 3. 常见数据结构
#     3.0 Strings
#     3.1 List
#     3.2 Tuples
#     3.3 Dictionaries
#     3.4 Sets

#######################################################################
## 0-0. 帮助文档的语法规范
### 例如：
help(list.pop)
# pop(...)
#   L.pop([index]) -> item -- remove and return item at index (default -1)
#   Raises IndexError if list is empty or index is out of range.
# (END)
# 解释：方括号里面的 index 表示可选变量，如果不填，则用其默认值（此处为-1)

help(list.sort)
# sort(...)
#   L.sort(cmp=None, key=None, reverse=False) -- stable sort *IN PLACE*;
#   cmp(x, y) -> -1, 0, 1
# (END)
# 解释：cmp, key, reverse 三个变量如果缺省的话，都用默认值；
# 注意：此方法是修改列表本身，无返回值

help(sorted)
# sorted(...)
#   sorted(iterable, cmp=None, key=None, reverse=False) --> new sorted list
# (END)
# 解释：此为内建函数，会生成新的 list 容器，即有返回值。
# key 的返回值是用于比较的对象，而 cmp 的返回则是用于比较的方法/手段。
# 注意：这里的 key, cmp 功能多用 lambda 函数去写！！

#=======================================================================#

## 0-1. sort() 举例说明，sort() 函数类比即可
# 实际上sort()方法在不传入参数func的时候 默认cmp为None
# 调用的是lambda x,y: cmp(x, y),而实际上就是调用cmp函数。即：
numbers = [5,2,9,7]
numbers.sort() 
    #sort()函数判断cmp为None，则调用`lambda x,y: cmp(x, y)`
numbers.sort(cmp=None) #等效于numbers.sort()
numbers.sort(cmp=cmp)
    #sort()判断cmp存在，并且不为None,则通过调用`cmp(x,y)`来排序
    #虽然结果是相同的，可实际执行流程是不同的
    #(这里我不确定sort()内部是用匿名函数还是直接用cmp来实现的)
numbers.sort(cmp) 
    #sort()通过*args来寻找是否存在没有指定变量的传入参数
    #函数判断其是否callalbe，如果是则赋值给cmp
    #函数执行`cmp(x,y)`来排序
numbers.sort(custom_sort_method) 
    #sort()通过*args来寻找是否存在没有指定变量的传入参数
    #函数判断其是否callalbe，即是否是函数
    #如果是则赋值给cmp = custom_sort_method
    #函数调用`cmp(x,y)`来排序
    #但此时的cmp实际上已经是custom_sort_method方法了
numbers.sort(cmp = custom_sort_method)
    #此时函数直接发现cmp不为None，则直接执行cmp函数来排序
    #而此时cmp也已经是custom_sort_method方法了

# 如果要实现自定义比较函数则需要重新指定cmp为你构造的比较函数，如下：
numbers = [5,2,9,7]
def reverse_numeric(x, y):
    return y - x
numbers.sort(cmp = reverse_numeric)
    #也可以直接写成
numbers.sort(revers_numeric)
    #或者直接传入匿名函数
numbers.sort(lambda x,y: y-x)
# 另外，在python3.x中取消了cmp参数，也不支持直接往sort()里面传函数了
# 可以构造排序函数传递给key来实现。

# 如果数组成员不是数字，而是其它的类型例如dict，想根据某个属性来排序:
company=[{'n':'Apple','y':10}, {'n':'IBM','y':8},{'n':'Google','y':12}]
## 数字排序：利用 cpm 表达式或者 key 表达式
sorted(company, cmp=lambda a,b:a['y']-b['y']) # 此处元素 a, b 为字典
# [{'y': 8, 'n': 'IBM'}, {'y': 10, 'n': 'Apple'}, {'y': 12, 'n': 'Google'}]
sorted(company, key = lambda a:str(a['y'])[-1]) # 利用'y'中数字的末位排序
# [{'y': 10, 'n': 'Apple'}, {'y': 12, 'n': 'Google'}, {'y': 8, 'n': 'IBM'}]
## 名称字母排序：利用 cmp 表达式或者 key 表达式
sorted(company, cmp=lambda a,b:cmp(a['n'],b['n'])) # 此处元素 a, b 为字典
# [{'y': 10, 'n': 'Apple'}, {'y': 12, 'n': 'Google'}, {'y': 8, 'n': 'IBM'}]
sorted(company, key = lambda a:a['n'][-3])  # 利用 'n' 键下的倒数3个字母排序
# [{'y': 8, 'n': 'IBM'}, {'y': 12, 'n': 'Google'}, {'y': 10, 'n': 'Apple'}]
#=======================================================================#

## 0-2. 其他注意点
print str(1)+'nihao'      # Python2的print不加括号，是个指令
eval(eval("'1'+'1'"))     # 11, 可以简单的理解为，eval用来剥掉最外层引号
str(1992)                 # '1992' 
repr(1992)                # '1992', 类似 str() 命令
# Example
class Person: 
    # ......
    # Use __repr__ to recreate the object
    def __repr__(self):   
        return "Person('" + self.name + "'," + str(self.age) + ")"
    # >>> print(repr(jenny))  # Person('Jennifer Jones',23)
    # >>> eval(repr(alex))    # Person('Jim Chi’,24)

### Python 中的拷贝
'''
Python 在所执行的复制动作中，如果是基本类型的数据 (比如 int,str)，就在内存中
重新建个窝，如果不是基本类型的，就不新建窝了，而是用标签引用原来的窝。这种拷贝
的方式称之为“浅拷贝”。

而在 Python 中，可以利用 import copy; x = copy.deepcopy(y) 来实现“深拷贝”。
'''

#######################################################################
## 1. 类型和内存地址，无需申明变量类型
id(3.33)                  # 4302350016
type(3.33)                # <class 'float'>
type(9999999999999999999) # <type 'long'>, 属于 int 
x = 5                     # 对象5有类型, 变量x无类型
a = 1; b = a; False if id(a)!=id(b) else True  # Ture, 变量是对象的标签

#######################################################################
## 2. 数学计算和模块使用
divmod(9,2)               # (4, 1), 除法用divmod
6 % 5                     # 1, 余数
round(2.249,2)            # 2.25, 四舍五入功能用round
round(2.235,2)            # 2.23, 十进制转二进制中出现的误差
import math; dir(math)    # dir(module_name)  
help(math.cos)            # help(module_name.method_name)
math.floor(3.92)          # 3.0
math.fmod(5,3)            # 2.0, 等价于 5%3
#from __future__ import division; 8/3  # 2.6666666666666665, 引入除法模块

    # 运算符                    描述（优先级从低到高）
    # lambda                    Lambda 表达式
    # or                        布尔“或”
    # and                       布尔“与”
    # not x                     布尔“非”
    # in，not in                成员测试
    # is，is not                同一性测试
    # <，<=，>，>=，!=，==       比较
    # |                         按位或
    # ^                         按位异或
    # &                         按位与
    # <<，>>                    移位
    # +，-                      加法与减法
    # *，/，%                   乘法、除法与取余
    # +x，-x                    正负号
    # ~x                        按位翻转
    # **                        指数
    # x.attribute               属性参考
    # x[index]                  下标
    # x[index:index]            寻址段
    # f(arguments...)           函数调用
    # (experession,...)         绑定或元组显示
    # [expression,...]          列表显示
    # {key:datum,...}           字典显示
    # 'expression,...'          字符串转换

#######################################################################
## 3. 常见数据结构

### 3.0 Strings
#### 编码问题
# -*- coding: utf-8 -*-                                 # 申明
import codecs; codecs.open('filename', encoding='utf8') # 打开文件

##### 字符串常用操作
print r"c:\news"             # r'strings' ----> 原始字符串
'abcdefg'.index('g')         # 6
len('abcdefg')               # 7
'abcdefg'[0:1]               # 'a', 半开区间
cmp('a','b'), cmp('a','a')   # (-1, 0)
min('abcdefg')               # 'a'
ord('a'), ord('A')           # (97, 65)
chr(ord('a')), chr(65)       # ('a','A')
a=' J '; a.strip(),a.lstrip(),a.rstrip()        # ('J', 'J ', ' J') 
print "# My name is {name} and I'm {age:5.2f} years old.{str}"\
.format(age = 18, name = 'Alex', str = "\n#"+"*"*70+"#\n")
# My name is Alex and I'm 18.00 years old.
#**********************************************************************#

#### 字符串中的 split 和 join 方法
#### String 和 list 的互相转化!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
'www.skip-lyy.com'.split(".")[1].split('-')[0]  # 'skip'
'fen ge\n fu\t doubei fen'.split() # ['fen', 'ge', 'fu', 'doubei', 'fen']
'*'.join('www.skip-lyy.com'.split("."))         # 'www*skip-lyy*com'

#### String 的正则分割！！！！！！！！！！！！！！！！！！！！！！！！！！
import re  # \s表示任何（单个）空字符，* 表示任意字符
str1 ='a,b c;d!e  f\ng'; str2 = '2016-06-06-15-48-12xxx_uploaded.png'
'-'.join(re.split(r'[\s,;!]*',str1)) # 'a-b-c-d-e-f-g'
':'.join(str2.split('_')[0].split('-')[-3:-1]) # '15:48'
# 更多见 http://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html

    # 转义字符    描述
    # \           在行尾时的续行符
    # \a          响铃
    # \b          退格(Backspace)
    # \000        空
    # \v          纵向制表符
    # \t          横向制表符
    # \r          回车
    # \f          换页

### 3.1 List
#### List 基础方法
list1 = [1,'2',[3],{4},5]
del list1[3:5]            # [1, '2', [3]]              删除元素，半开区间
list1.extend([4,5])       # [1, '2', [3], set([4]), 5, 4, 5]    合并列表
2 in list1                # False                               检查元素
len(list1)                # 7                                   测量长度
ori=[1,2,3,4,5]; ori[::2] # ([1, 3, 5], [1, 2, 3, 4, 5])        取元素
ori[::-1],ori             # ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5])  倒序
list(reversed(ori)),ori   # ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5])  倒序
[1,1,22,3,4].count(1)     # 2, 计数
[1,1,22,3,4].index(1)     # 0, 给最小的index号码，元素没有的话就ValueError
# 关于 index 下的 ValueError 的应用，举例如下：
lst = [0,2,1,3,3,2]
for num in range(len(lst)):
    try:
        print num,"'s lowest index: ",lst.index(num)
    except ValueError:
        print "There's no ",num 
# 0 's lowest index:  0
# 1 's lowest index:  2
# 2 's lowest index:  1
# 3 's lowest index:  3
# 4 's lowest index:  There's no  4
# 5 's lowest index:  There's no  5

# 插入和删除
lst = ["1","2"]; lst.insert(0,"0")   # ["0", 1", "2"], 插入到索引位置
lst = ["1","2"]; lst.insert(100,"3") # ["1", "2", "3"], 超过最大索引则追加
lst = ["1","2","1"]; lst.remove("1") # ["2", "1"]
lst = ["1","2","1"]; lst.remove("3") # ValueError
lst = ["1","2","3"]; lst.pop()       # ["1", "2"], i 默认为 -1
lst = ["1","2","3"]; lst.pop(1)      # ["1", "3"]

# 排序问题
lst = [0,1,2,3]; lst.reverse(); lst         # [3, 2, 1, 0]
lst = [0,1,2,3];new = lst[::-1]
lst,new                                   # ([0, 1, 2, 3], [3, 2, 1, 0])

# sort() 方法和 sorted() 函数
# list.sort()方法只为list定义，而sorted()函数可以接收任何的iterable
lst = [0,1]; lst.sort(); lst                # [0, 1], sort 默认从小到大
lst = [0,1]; lst.sort(reverse = True); lst  # [1, 0], sort 的参数设置
sorted([1,2,3,0,5,3,2])                          # [0, 1, 2, 2, 3, 3, 5]
sorted({4: 'D', 2: 'B', 3: 'B', 5: 'E', 1: 'A'}) # [1, 2, 3, 4, 5]
sorted('A,bb,aa,CCC'.split(','), key = str.lower, reverse = True) 
# ['CCC', 'bb', 'aa', 'A'], 按照字母的小写编码进行从大到小排列

##### List 简易循环
sumnum = 0
for num in range(10):                        # List 中的最简易的循环方式
    sumnum += num 

#### List 增长列表
a = [1,2,3,4]; 
id(a)                               # 4347015536
a.append('5')                       # [1, 2, 3, 4, '5']         添加元素
a[len(a):] = ['6']                  # [1, 2, 3, 4, '5', '6']    添加元素
#       |    |   |
#      冒号   列表括号
a.extend([7,8]) # [1, 2, 3, 4, '5', '6', 7, 8]              列表直接接上
a.extend("abc") # [1, 2, 3, 4, '5', '6', 7, 8, 'a', 'b', 'c'] 字符串拆分
id(a)                               # 4347015536, 地址不变
# 对于 append()和 extend()，它们都是原地修改列表，都没有返回值！！！！！！
# 因为没有返回值，所以例如 a = [1,2,3].extend([4,5]) 的赋值是没有意义的！

#### append 与 extend 的区别
[1,2,3].append(['4','5'])  # [1, 2, 3, ['4', '5']], 一次性添加
[1,2,3].append('nihao')    # [1, 2, 3, 'nihao'], 一次性添加
[1,2,3].extend(['4','5'])  # [1, 2, 3, '4', '5'], 拆分添加
[1,2,3].extend('nihao')    # [1, 2, 3, 'n', 'i', 'h', 'a', 'o'], 拆分添加

#**********************************************************************#
### 3.2 Tuples
tup = (1, "2", (3,3))# 元素多样性，近list，hashable type!!!!!!!!!!!!!!!
tup[0] = 3           # Raises a TypeError, 不能原地修改，近string
a, b, c = (1, 2, 3)  # You can unpack tuples (or lists) into variables
d, e, f = 4, 5, 6    # Tuples are created by default if no parentheses
e, d = d, e          # d is now 5 and e is now 4
type((3)),type((3,)) # (<type 'int'>, <type 'tuple'>), 单元素Tuple加逗号

#### Tuple 和 List 的转化
list((1,'2',(3,)))   # [1, '2', (3,)]
True if tuple(list((1,'2',(3,)))) == (1,'2',(3,)) else False # True

#### Tuple 的使用场景:
'''
1、 Tuple 比 list 操作速度快。如果您定义了一个值的常量集，并且唯一要用它做的
    是不断地遍历它，请使用 tuple 代替 list。
2、如果对不需要修改的数据进行 “写保护”，可以使代码更安全。使用 tuple 而不是
    list 如同拥有一个隐含的 assert 语句，说明这一数据是常量。如果必须要改变
    这些值，则需要执行 tuple 到 list 的转换 (需要使用一个特殊的函数)。
3、Tuples 可以在 dictionary（字典，后面要讲述） 中被用做 key，但是 list不行。
    Dictionary key 必须是不可变的。Tuple 本身是不可改变的，但是如果您有一个 
    list 的 tuple，那就认为是可变的了，用做 dictionary key 就是不安全的。只有
    字符串、整数或其它对 dictionary 安全的 tuple 才可以用作 dictionary key。
    Tuples 可以用在字符串格式化中。
'''

#**********************************************************************#
### 3.3 Dictionaries

#### 创建字典
dict0 = {}                                   # 创建空字典
dict1 = {"one": 1, "two": 2, "three": 3}     # 直接创建
dict2 = dict(one = 1, two =2, three = 3)     # 直接创建
dict3 = dict((['one',1],['two',2],['three',3])) # 利用 Tuple 创建 
dict4 = {(1,1):1,'2':2} # {'2': 2, (1, 1): 1}, key 可以用 tuple，不能list

#### 查看字典
dict1["one"]         # 1, 使用 [] 来查询键值
dict1["four"]        # KeyError
dict1.get("one")     # 1
dict1.get("four")    # None，避免了KeyError
dict1.get("four", 'HI') # 'HI'，get 方法支持传入一个默认值参数，将在取不到值时返回
"one" in dict1       # True，使用 in 来检查一个字典是否包含某个键名
dict1.has_key('one') # 同上
1 in dict1           # False

dict1.keys()     # ["three", "two", "one"], 无顺序，键名返回形式列表!!!!!!!
dict1.values()   # [3, 2, 1]， 顺序与上述对应,键值返回形式列表!!!!!!!!!!!!!!
dict1.items()    # [('three', 3), ('two', 2), ('one', 1)], 返回形式列表!!!!
### 对于需要迭代的字典对象，可利用keys, values, items的iter前缀以提升迭代速率
type(dict1.iterkeys()) # <type 'dictionary-keyiterator'>
list(dict1.iteritems()) # [('three', 3), ('two', 2), ('one', 1)]

#### 添加/删除字典中的键/清空字典 (字典里面的 keys 不会重复，但 values 可能)
dict1.setdefault("five", 5) #dict1["five"] is set to 5
dict1.setdefault("five", 6) #dict1["five"] is still 5，安全添加新的值
del dict1['five']
dict1.pop['three']     # 3, 用 pop 的方式删除元素，删除后会返回被删除的value
dict1.clear()          # dict1={}
dict1.update(dict2)    # 把 dict2 更新到 dict1 中，若key相同，则velue用dict2的

#### 字典的使用
'''
dict 中的这类以键值对的映射方式存储数据，是一种非常高效的方法，比如要读取值得时候，
如果用列表，Python 需要从头开始读，直到找到指定的那个索引值。但是，在 dict 中是通过
“键”来得到值。要高效得多。 正是这个特点，键值对这样的形式可以用来存储大规模的数据，
因为检索快捷。规模越大越明显。所以，mongdb 这种非关系型数据库在大数据方面比较流行了。
'''

#### 哈希
'''
散列表（Hash table，也叫哈希表），是根据关键字（Key value）而直接访问在内存存储
位置的数据结构。也就是说，它通过把键值通过一个函数的计算，映射到表中一个位置来访
问记录，这加快了查找速度。这个映射函数称做散列函数，存放记录的数组称做散列表。

字典dict，是Python唯一的标准mapping类型，也是内置在Python解释器中的。
mapping object把一个可哈希的值（hashable value）映射到一个任意的object上。
那什么是可哈希的？一个object是可哈希的（hashable）， 是指这个object在其生存期内
有一个不变的哈希值（hash value），即__hash__()方法返回的值。所有不可变的（immutable）
内置object都是hashable的，比如string，tuple。所有可变的（mutable）内置容器都不是
hashable的，比如list，dict（即没有__hash__()方法）。而所有自定义（use-defined class）
对象都是可哈希的（hashable），并且只能和自己相等，其hashvalue为其id(object)的值。

总结：字典Dictionary的key必须是可哈希的，所以tuple，string可以做key，而list不能做key。
'''

#### 举例
temp = "<html><head><title>%(lang)s<title><body><p>My name is %(name)s.</p></body></head></html>"
my = {"name":"Jim", "lang":"Python"}
temp % my
# '<html><head><title>python<title><body><p>My name is qiwsir.</p></body></head></html>'


#**********************************************************************#
### 3.4.1 Unhashable set

#### Set 的创建：最好用set()，不提倡用空{}的方式，会跟dict混淆！！！！！！！
s1 = set ("Hello")   # set(['H', 'e', 'l', 'o']), 注意只有一个'l', 不重复
s2 = {(1,2,3,4)}     # set([1, 2, 3, 4])
s2 = {1,2,3,4}       # set([1, 2, 3, 4])
s3 = {[1,2,3,4]}     # TypeError: unhashable type: 'list'
s4 = {(set([1, 2, 3, 4]))} # TypeError: unhashable type: 'set'
## 总结，可 set 的对象必须是 hashable 的，list和set本身不可哈希，所以报错；
## 区别：set([1, 2, 3, 4]) 或者 set(set([1,2,3,4])) 表达的就是 (1,2,3,4)
## 这个set，类比于set(['n','y']), 不能理解为把列表[1,2,3,4] 作为 set 的对象，
## 因为不存在这种可能，list 本身就是不可哈希的！

#### Set 与 list 的转化
list(set('chi'))   # ['i', 'h', 'c']

#### Set 的方法
dir(set)
['__and__', '__class__', '__cmp__', '__contains__', '__delattr__', \
'__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__',\
 '__hash__', '__iand__', '__init__', '__ior__', '__isub__', '__iter__', \
 '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__',\
 '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', \
 '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__',\
 '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', \
 'difference_update', 'discard', 'intersection', 'intersection_update', \
 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', \
 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']

#### 增加 set 元素
s1  = set('1234')     # set(['1', '3', '2', '4'])
s1.add('567')         # set(['1', '3', '2', '4', '567'])
s1.add([8,9])         # TypeError: unhashable type: 'list'
s1.add('[8,9]')       # set(['[8,9]', '567', '1', '3', '2', '4'])
s1.add(10)            # set(['[8,9]', '567', '1', '3', '2', '4', 10])
s1.update(set('000')) # set(['[8,9]', '567', '1', '3', '2', '4', 10, '0'])

### 3.4.2 Hashable set
f_set = frozenset("12334") # frozenset(['1', '3', '2', '4'])
f_set.add("python")        # AttributeError, 不能add，即不能原地修改

### 3.4.3 集合运算
A = set('01234'); B = set('12345')
A < B, A == B, A > B        # (False, False, False)
A|B                         # set(['1', '0', '3', '2', '5', '4']), 并集
A&B                         # set(['1', '3', '2', '4']), 交集
A-B                         # set(['0']), A有而B没有的

#### 删除 set元素：pop, remove, discard, clear 
# set.pop()是从 set 中任意选一个元素,删除并将这个值返回
# set.remove(obj)中的 obj，必须是 set 中的元素，否则就报错
# set.discard(obj)中的 obj 如果是 set 中的元素就删除，如果不是就什么也不做
# set.clear() 的功能是 Remove all elements from this set

#######################################################################
# 总结
# 1、查看使用方法和定义：
#      交互模式下用 dir()或者 help() 或者使用 Google
# 2、数据类型中：
#      能够索引的，如 list/str，其中的元素可以重复
#      可变的，如 list/dict，即其中的元素/键值对可以原地修改
#      不可变的，如 str/int，即不能进行原地修改
#      无索引序列的，如 dict、set，即其中的元素（键值对）没有排列顺序
