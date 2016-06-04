# -*- coding:utf-8 -*- 

# @Ji Chi
# 18:25, 4 Jun 2016

class Person: 
    '''This is the documentation strings'''
    # Use __doc__ to show documentation strings
    # >>> jenny.__doc__   # 'This is the documentation strings'
    
    # Use __init__ to initialize
    def __init__(self, name, age): 
        self.name = name  
        self.age = age 

    ########## Attributes
    species = 'human'
    def get_species():
        return Person.species
    ########## Functions
    def get_older(self, n = 1):  
        self.age += n 
        return self.age 

    def get_first_name(self): 
        return self.name.split()[0]

    ############ Special functions 
    # Use __str__ to print or str some info
    def __str__(self):    
        return self.name
    # >>> print(alex)  # Jim Chi
    # >>> str(alex)    # 'Jim Chi'
    
    # Use __repr__ to recreate the object
    def __repr__(self):   
        return "Person('" + self.name + "'," + str(self.age) + ")"
    # >>> print(repr(jenny))  # Person('Jennifer Jones',23)
    # >>> eval(repr(alex))    # Person('Jim Chi’,24)

    ############ Special functions: __name__
    # 1\ 如果直接运行包含此 Person class 的py程序，则 __name__ ＝ '__main__'
    # 2\ 如果是 import 的此 Person class，则 Person.__name__ ＝ 'Person'

class Employee(Person):   
    # do not directly use __init__, add super() as a prefix
    def __init__(self, name, role):  
        super().__init__(name, -1)   
        self.role = role 
        self.age = 'irrelevant'

    def __str__(self): 
        if self.role == 'professor':
            return 'Dr. ' + self.name 
        else: 
            return self.name

def main():
    import time
    print('{0}{1}{2}'.format('''    This is a small program to test the functions/methods
    and variables of class/subclass in Python.\n''','    ',time.strftime("%Y-%m-%d %H:%M:%S %Z", time.localtime())))
    msg = input('\nInput your name,age,role: \n(format like：Jon Snow,18,Night\'s Watch)\n')
    # print(msg.split(",")) 
    you1 = Person(msg.split(",")[0],int(msg.split(",")[1]))
    you2 = Employee(msg.split(",")[0],msg.split(",")[2])
    print('{0}{1}{2}{3}{4}'.format('Hello ',you2,'. Your age is ',you1.age,', right?'))

if __name__ == '__main__':
    main()
