# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 22:13:12 2022

@author: Suyog
Day 2 Project Assignment:

PROJECT :

Let's say, you are in a lottery competition. A group of words has been given to you and you are asked to select any one character(only alphabets) which will get you a prize. You are a smart person and you thought of a way to select a character that will have maximum chances of winning a prize i.e. select the highest occurring character from the words.


Given this situation you are required to write a code in Python that will select a character from the words that occurs the most.

Note:

Prizes may be allotted to the characters in any manner (sequential or alternate or any other way). Some characters may not be entitled for any prize.
Ignore spaces and other special character. Consider only alphabets for prizes.
Assume that all characters will be in lowercase.

Example:

Word Given: hello coders

If Index of characters assigned with prize are as below: 0, 1, 4, 6, 8

Then if you choose the characters at the above indices, only then you will win a prize.

Selecting any of the following characters 'h' or 'e' or 'o' or 'c' or 'd' will only get you a prize.
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