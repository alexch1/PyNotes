# -*- coding:utf-8 -*- 

'''
Created on 20 May 2016

This is a simple program helping to find the prime numbers below a threshold.
Some basic Functions/Control Statements for Python are also tested here.

@author: alexchi
'''

 
def getthreshold():
    '''
    get the length from input and generate an int random value with the specific legth.

    '''

    choice = int(input('\nChoose the type (1 or 2):\n1. set a specific threshold number\n2. Randomly generated a threshold\n'))
    if choice == 1:
        number = int(input('\nPlease input your threshold number:\n'))        
    else:
        length = int(input('\nSet the length of your threshold number:\n'))
        from random import randint
        # uniform gives you a floating-point value
        number = randint(10 **(length-1), 10 ** length)
        print "\nThe threshold value is randomly set to be:", number
    return number
 
def print_prime_numbers(threshold):
    import math
    for num in range(1,threshold+1):
        flag = True
        
        for divnum in range(1,int(math.sqrt(num))+1):
            if (num % divnum == 0) and (divnum != num) and (divnum != 1):
                flag = False
                break
        if flag == True:
            print num

print "\nThis is a program helping you to find the prime numbers below a certain threshold."
threshold = getthreshold()
print "\nThe prime numbers below the threshold", threshold, "are shown below:"
print_prime_numbers(threshold)
print "\n"
