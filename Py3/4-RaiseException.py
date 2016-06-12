# -*- coding:utf-8 -*- 
 
def first_asterisk(s):
    """Returns the index of the first '*' in a string."""
    # require('*' in s)    
    for index in range(0, len(s)):
        if s[index] == '*':
            break
    assert s[index] == '*', "No asterisk found in the string!"
    assert '*' not in s[index+1:], "More than one asterisk in the string!"
    return index
 
def square_root(n):
    """Finds the square root of a non-negative number."""
    if n < 0:       # 负数的话会 raise Expection
        raise Exception("square_root called with " + str(n))
    epsilon = 0.0000001
    guess = n / 2
    quotient = n / guess
    while abs(quotient - guess) > epsilon:
        guess = (guess + quotient) / 2
        quotient = n / guess
    return guess
 
def mian():
    def find_asterisk():
        try:
            print("The index of asterisk is:",first_asterisk(input("Please input a string with one sterisk:\n")))
        except AssertionError as msg:
            print(msg,"Please try again\n")
            return find_asterisk()
 
    def find_square_root():
        try:
            print("The square root is",square_root(int(input("Please input a non-negative value:\n"))))
        except Exception as msg:
            print(msg,". Please try again\n")
            return find_square_root()
 
    find_asterisk()
    find_square_root()
    print('All done!')   # 负数的话不会显示，因为上一句已经 raise Exception 了
 
if __name__ == '__main__':
    mian()
