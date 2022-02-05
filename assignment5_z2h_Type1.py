# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 15:41:57 2022

@author: Suyog
Assignment: Use filter function to filter out the elements from a list that are divisible by 3 & 5
(Using filter function)
"""


def divisibility_func(Number):
        if (Number%3==0 and Number%5==0):
            return True
        else:
            return False

# sequence
My_list = []
for i in range(1,101,1):
     My_list.append(i)
     print(i)
# using filter function
filtered = filter(divisibility_func, My_list)

print('The filtered numbers divisible by 3 and 5 are:')
for s in filtered:
	print(s)
