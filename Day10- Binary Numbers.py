# -*- coding: utf-8 -*-
"""
Created on Sat May 22 23:31:13 2021

@author: Meenal
"""

#Task
#Given a base-10 integer, n , convert it to binary (base-2). Then find and print the base-10 integer denoting the maximum number of consecutive 1's in n's binary representation. When working with different bases, it is common to show the base as a subscript.

#Example
#n=125

#The binary representation of (125)base10 is (1111101)base2. In base 10, there are 5 and 1 consecutive ones in two groups. Print the maximum,5 .

#Input Format
#A single integer,n .

#Constraints
#1<=n<10^6

#Output Format
#Print a single base-10 integer that denotes the maximum number of consecutive 1's in the binary representation of n.

#Sample Input 1
#5
#Sample Output 1
#1

if __name__ == '__main__':
    a=[]
    n = int(input().strip())
    while(n!=0):
        r=n%2
        a.append(int(r))
        n=n//2
    a.reverse()
    c=0
    d=0
    for i in range(len(a)):
        if(a[i]==1):
            c+=1
        if(a[i]==0):
            break
    for i in range(len(a)-1,-1,-1):
        if(a[i]==1):
            d+=1
        if(a[i]==0):
            break  
    if(c>d):   
        print(c)
    else:
        print(d)