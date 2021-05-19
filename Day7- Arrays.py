# -*- coding: utf-8 -*-
"""
Created on Wed May 19 14:20:51 2021

@author: Meenal
"""

# Day 7: Arrays

# Task 
# Given an array, A, of N integers, print A's elements in reverse order as a single line of space-separated numbers.

# Input Format
# The first line contains an integer, N (the size of our array). 
# The second line contains N space-separated integers describing array A's elements.

# Constraints
# 1 <= N <= 1000
# 1 <= Ai <= 10000, where Ai is the ith integer in the array

# Output Format
# Print the elements of array A in reverse order as a single line of space-separated numbers.

#!/bin/python
#Sample Input

#4
#1 4 3 2
#Sample Output

#2 3 4 1

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    l=len(arr)
    for i in range (l-1,-1,-1):
        print(arr[i],end=" ")