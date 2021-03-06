# -*- coding: utf-8 -*-
"""
Created on Wed May 19 13:32:24 2021

@author: Meenal
"""

#Task
#Write a Person class with an instance variable, age, and a constructor that takes an integer,initialAge , as a parameter. The constructor must assign initialAge to age after confirming the argument passed as initialAge is not negative; if a negative argument is passed as initialAge , the constructor should set age to 0  and print Age is not valid, setting age to 0.. In addition, you must write the following instance methods:

#yearPasses() should increase the age instance variable by 1 .
#amIOld() should perform the following conditional actions:
#If age<13, print You are young..
#If  age>=13 and age<18, print You are a teenager..
#Otherwise, print You are old..
#To help you learn by example and complete this challenge, much of the code is provided for you, but you'll be writing everything in the future. The code that creates each instance of your Person class is in the main method. Don't worry if you don't understand it all quite yet!

#Note: Do not remove or alter the stub code in the editor.

#Input Format

#Input is handled for you by the stub code in the editor.

#The first line contains an integer,  (the number of test cases), and the  subsequent lines each contain an integer denoting the  of a Person instance.


#Output Format

#Complete the method definitions provided in the editor so they meet the specifications outlined above; the code to test your work is already in the editor. If your methods are implemented correctly, each test case will print  or  lines (depending on whether or not a valid  was passed to the constructor).

#Sample Input
#4
#-1
#10
#16
#18

#Sample Output
#Age is not valid, setting age to 0.
#You are young.
#You are young.

#You are young.
#You are a teenager.

#You are a teenager.
#You are old.

#You are old.
#You are old.


class Person:
    age=0
    def __init__(self,initialAge):
        if(initialAge<0):
            self.age=0;
            print("Age is not valid, setting age to 0.\n",end="")
        
        else:
            self.age=initialAge;
        # Add some more code to run some checks on initialAge
    def amIOld(self):
        if(self.age<13):
            print("You are young.\n",end="")
        if(self.age>=13 and self.age<18):
            print("You are a teenager.\n",end="");
        if(self.age>=18):
            print("You are old.\n",end="");
        # Do some computations in here and print out the correct statement to the console
    def yearPasses(self):
        self.age+=1;
        # Increment the age of the person in here

t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")