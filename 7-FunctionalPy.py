######## iterator
# next(iter({'one', 'two', 'three', 'four'}))  # set
# next(iter(('one', 'two', 'three', 'four')))  # tuple
# next(iter('one two three four'))             # string
# next(iter({'one': 'two', 'three': 'four'}))  # dictionary
# next(iter(range(5, 10)))                     # range
# next(iter(open('testfile.txt', 'r')))        # file

def file_len(full_path):
  """ Count number of lines in a file."""
  f = open(full_path)
  nr_of_lines = sum(1 for line in f)
  f.close()
  return nr_of_lines

import os
os.chdir("../Desktop")
fp = open("test.txt","w")
for index in range(1,5):
    fp.writelines('{}{}'.format(str(index),": Hello Word!\n"))
fp.close()
len = file_len('test.txt')

print('Method 1\n')
fp = open("test.txt","r")
it = iter(fp)
for line in range(1,len+1):
    print(next(it))
fp.close()

print('Method 2\n')
with open('test.txt') as fp:
    f = fp.readlines()
    for line in range(0,len):
        print(f[line])
fp.close()

print('Method 3\n')
with open('test.txt') as fp:
    for line in range(0,len):
        print(fp.readline())
fp.close()

######## lambda expression (e.g., map(), filter(), functools.reduce() etc.)

# good usage
print(sorted([('a', 3), ('b', 2), ('c', 1)], key=lambda x:x[1]))
# >>>[('c', 1), ('b', 2), ('a', 3)]

# silly usage
(lambda x: x[1]*x[2])([1,2,3,4])
# >>>6

# map(function, sequence)
# different from Py 2.x, in Py 3.x, use list before map()
map(lambda x : x*2, [1, 2, 3, 4, 5])
list(map(lambda x : x*2, [1, 2, 3, 4, 5]))
# >>>[2, 4, 6, 8, 10]

# filter(predicate, sequence)
# different from Py 2.x, in Py 3.x, use list before filter()
filter(lambda x: x % 2 != 0  and x % 3 != 0, range(2, 25))
list(filter(lambda x: x % 2 != 0  and x % 3 != 0, range(2, 25)))
# >>>[5, 7, 11, 13, 17, 19, 23]

# functools.reduce(binaryFunction, finiteSequence)
# firstly, first 2 elements; then, result and next element
import functools
functools.reduce(lambda x, y: x - y, [100, 1, 2, 3])
(((100 - 1) -2) -3)
# >>> 94


######## conditional expressions
# Syntax: expression1 if condition else expression2 

print(100+(5 if 2>3 else 7))
# >>>107

print('Hi boy' if input('Are you a boy?(y/n)\n')=='y' else 'Hi girl')
# >>> input y ~ Hi boy... input n ~ Hi girl


######## any, all, some, forall
# any(iterable) returns True if any element is 'truthy'
any([0,False,[],''])
# >>> False
any([0,False,[],'','Hi'])
# >>> True

# all(iterable) returns True if every element is 'truthy'
all(['hi',True,[3],333])
# >>> True
all(['hi',True,[3],333,2>6])
# >>> False

def forall(f, s): return all(map(f, s))
forall(lambda x: x > 0, [1, 2, 3])     # True
forall(lambda x: x > 0, [1, -2, 3])    # False

def some(f, s): return any(map(f, s))
some(lambda x: x in 'aeiou', 'frog')   # True
some(lambda x: x in 'aeiou', 'fly')    # False

######## Q?
for i in (lambda x:x**i for i in range(3)):
    print (i(4)) 
# >>> 1 
# >>> 14
# >>> 16
