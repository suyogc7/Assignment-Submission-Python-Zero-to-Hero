# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 22:03:49 2022

@author: Suyog
Day 4 Assignment:

Define a function which will take a number as argument and return its factorial.

Call the function to print factorial of any number(integer).
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Input a number to compute the factorial: "))
print("The factorial of %d is %d"%(n,factorial(n)))