# Author: Ken Obata
# Created Date: December, 26, 2019
# Description:
# This program reads comman line input from user to calculate derangement of integer.
# derangement is a permutation with condition that no object is in its own possition.
# Formula is derangement(x) = x!*[sum((-1)^i * (1/i!) )] | i = 0 to x

# Ex) derangement(4) = 4!*[1 - 1/1! + 1/2! - 1/3! + 1/4!]
#                    = 24 - 24 + 12 - 4 +1
#                    = 9

from fractions import Fraction
import math


def derangement(n):
    temp=math.factorial(n)
    
    for i in range(1,n+1):
        if(i % 2 != 0 ):#if odd, subtract
            temp -= math.factorial(n)*Fraction(1, math.factorial(i))
        
        else:# if even, add.
            temp += math.factorial(n)*Fraction(1, math.factorial(i))

    return temp

print("please input integer to calculate derangement.")
x = input()
print("derangement({}): {}".format(x, derangement(x)))
