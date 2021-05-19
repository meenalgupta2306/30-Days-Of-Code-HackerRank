# -*- coding: utf-8 -*-
"""
Created on Wed May 19 13:56:25 2021

@author: Meenal
"""

#Task
#Given an integer, , print its first  multiples. Each multiple  (where ) should be printed on a new line in the form: n x i = result.

#Example n=3

#The printout should look like this:

#3 x 1 = 3
#3 x 2 = 6
#3 x 3 = 9
#3 x 4 = 12
#3 x 5 = 15
#3 x 6 = 18
#3 x 7 = 21
#3 x 8 = 24
#3 x 9 = 27
#3 x 10 = 30


if __name__ == '__main__':
    n = int(input().strip())
    for i in range(1,11):
        print(n,"x",i,"=",n*i,end="\n")