# -*- coding: utf-8 -*-
"""
Created on Wed May 19 13:27:48 2021

@author: Meenal
"""

#Task
#Given an integer,n , perform the following conditional actions:

#If n is odd, print Weird
#If n is even and in the inclusive range of  to , print Not Weird
#If n is even and in the inclusive range of  to , print Weird
#If n is even and greater than , print Not Weird
#Complete the stub code provided in your editor to print whether or not  is weird.

#Input Format
#A single line containing a positive integer, .

#Constraints
#1<=n<=100
#Output Format

#Print Weird if the number is weird; otherwise, print Not Weird.

#Sample Input 0

#3
#Sample Output 0

#Weird


if __name__ == '__main__':
    n = int(input().strip())
    if(n%2!=0):
        print("Weird")
    if(n%2==0):
        if(n>=2 and n<=5):
            print("Not Weird")
        if(n>=6 and n<=20):
            print("Weird")
        else:
            print("Not Weird")