# -*- coding:utf-8 -*-   
 
######### Using String.Format #########
# Example:
# '{0}{2:10.3f}{1:10.3e}'.format("a",100,20)
#   |  |        |   
#   a 20       "a"
# Where 10.3 means width.precision, f and e mean float and e
# The display shall be:
# a    20.000 1.000e+02
 
def info():
    import time
    print('\t{0}{2}\t{1}'.format('INFO: from AlexCh1,','''
    ---------------------------------------------------
    | - This is a small program to sum up every       |
    |       digit from the input digital number.      |
    | - You need to input 3 digit numbers in total.   |
    | - For testing error msgs and reinput function,  |
    |       plz input an non-digital-numebr string.   |
    ---------------------------------------------------''',
    time.strftime("%Y-%m-%d %H:%M:%S %Z", time.localtime())))
 
def sum_digits():
    try:
        for i in range(0,3):
            num = input('{0}{1:0}{2:}'.format("\nInput no.",i+1," number:\n"))
            if not num.isdigit():
                raise Exception ('{0}{1}{2}'.format("Your input: \"",num,"\""))
            sum = 0
            for ele in range(len(num)):
                sum += int(num[ele])
            print('{0:15}{1}{2:0.2f}'.format('+'.join(num),'=',sum)) 
    except Exception as msg:
        print(msg,"\nPlease input digital numbers")
        return sum_digits()
    return
 
def mian():
    info()
    sum_digits()
    print("\nDone!")
 
if __name__ == '__main__':
    mian()
