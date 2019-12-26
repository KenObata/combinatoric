# Author: Ken Obata
# Created Date: December, 26, 2019
# Description:
# This program reads following comman line input from user
# to calculate number of onto function.
# input = m , n where m is number of distinct object to distribute
# n is number of distinct boxes(containers) to sotre m objects.
# This program returns stirling number's second kind,
# so no box is left empty.
# and all m object is distributed.
# In short, "order does not matter, and repeatition is allowed."


from fractions import Fraction
import math


def n_choose_k(n,k):
    return math.factorial(n) / math.factorial(k)\
        / math.factorial(n - k)


def stirling(m,n):
    temp=pow(n,m)
    
    for i in range(1, n):
        if(i % 2 != 0 ):#if odd, subtract
            temp -= n_choose_k(n,i)*pow((n - i), m)
        
        else:# if even, add.
            temp += n_choose_k(n,i)*pow((n - i), m)

    return temp/math.factorial(n)

print("please input number of m distinct objects to distribute.")
m = int(input())
print("please input number of n distinct boxes.")
n = int(input())
print("Stirling's number of 2nd kind, {} distinct object into {} boxes: {}".format(m, n, stirling(m,n)))

