# -*- coding: utf-8 -*-
"""
Created on Sat May 22 23:42:12 2021

@author: Meenal
"""

#Objective
#Today, we are building on our knowledge of arrays by adding another dimension. Check out the Tutorial tab for learning materials and an instructional video.

#Context
#Given a 6 x 6 2D Array, A :

#1 1 1 0 0 0
#0 1 0 0 0 0
#1 1 1 0 0 0
#0 0 0 0 0 0
#0 0 0 0 0 0
#0 0 0 0 0 0
#We define an hourglass in A to be a subset of values with indices falling in this pattern in A's graphical representation:

#a b c
#  d
#e f g
#There are 16 hourglasses in A, and an hourglass sum is the sum of an hourglass' values.

#Task
#Calculate the hourglass sum for every hourglass in A, then print the maximum hourglass sum.



if __name__ == '__main__':

    arr = []
    a=[]
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    for i in range(4):
        for j in range(4):
            sum=arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            a.append(sum)
    print(max(a))
