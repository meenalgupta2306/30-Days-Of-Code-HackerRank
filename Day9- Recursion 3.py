# -*- coding: utf-8 -*-
"""
Created on Wed May 19 15:22:44 2021

@author: Meenal
"""

#Recursive Method for Calculating Factorial
# factorial(n)= 1                         n<=1
             #= n* factorial(n-1)         otherwise
#Function Description
#Complete the factorial function in the editor below. Be sure to use recursion.

#factorial has the following paramter:

#int n: an integer
#Returns

#int: the factorial of n
#Note: If you fail to use recursion or fail to name your recursive function factorial or Factorial, you will get a score of .

#Input Format
#A single integer, n (the argument to pass to factorial).

#Constraints
#2<=n<=12
#Your submission must contain a recursive function named factorial.



def factorial(n):
    if(n<=1):
        return 1
    else:
        return (n* factorial(n-1))
    # Write your code here

n = int(input().strip())
print(factorial(n))
