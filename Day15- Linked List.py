# -*- coding: utf-8 -*-
"""
Created on Sun May 30 00:51:41 2021

@author: Meenal
"""

#Objective
#Today we will work with a Linked List. Check out the Tutorial tab for learning materials and an instructional video.

#A Node class is provided for you in the editor. A Node object has an integer data field, data, and a Node instance pointer, next, pointing to another node (i.e.: the next node in the list).

#A Node insert function is also declared in your editor. It has two parameters: a pointer, head, pointing to the first node of a linked list, and an integer,data , that must be added to the end of the list as a new Node object.

#Task
#Complete the insert function in your editor so that it creates a new Node (pass data as the Node constructor argument) and inserts it at the tail of the linked list referenced by the head parameter. Once the new node is added, return the reference to the head node.

#Note: The head argument is null for an empty list.

#Input Format

#The first line contains T, the number of elements to insert.
#Each of the next T lines contains an integer to insert at the end of the list.

#Output Format

#Return a reference to the head node of the linked list.


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data): 
    #Complete this method
        if head==None:
            head=Node(data)
        else:
            current=head
            while current.next:
                current=current.next
                
            current.next=Node(data)
        return head
mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 