# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 22:13:12 2022

@author: Suyog
"""

word = input("Please Enter the group of words (To be entered by the Lottery Officers):").lower()
# This string will be entered by the Lottery Officers
arr = []

for i in word:
    arr.append(i)

print(arr)
res2 = max(arr,key = arr.count)
print("The maximum occuring character is:"+ res2)
print("I select the character %s from the given sequence %s for the lottery."%(res2,word))