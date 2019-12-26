# Author: Ken Obata
# Created Date: December, 26, 2019
# Description:
# This program reads following comman line input from user
# to calculate number of onto function.
# input = m , n where m is number of distinct object to distribute
# n is number of distinct boxes(containers) to sotre m objects.
# This program is onto function, so no box is left empty.
# and all m object is distributed.
# In short, "order matters, and repeatition is allowed."


from fractions import Fraction
import math


def n_choose_k(n,k):
    return math.factorial(n) / math.factorial(k)\
        / math.factorial(n - k)


def onto(m,n):
    temp=pow(n,m)
    
    for i in range(1, n):
        if(i % 2 != 0 ):#if odd, subtract
            temp -= n_choose_k(n,i)*pow((n - i), m)
        
        else:# if even, add.
            temp += n_choose_k(n,i)*pow((n - i), m)


    return temp

print("please input number of m distinct objects to distribute.")
m = int(input())
print("please input number of n distinct boxes.")
n = int(input())
print("Onto function, {} distinct object into {} boxes: {}".format(m, n, onto(m,n)))
