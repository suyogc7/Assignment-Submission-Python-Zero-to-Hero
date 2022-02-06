# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 12:44:28 2022

@author: Suyog
"""

# Day 6 Assignment 
#Write a decorator, mod_div() that will add a feature to the above function 
#which will make sure that numerator will be always greater than the denominator.

def decorators(fun):
	def mod_div(number1, number2):
		if number1 < number2 :
			number1, number2 = number2, number1
		return fun(number1, number2)
	return mod_div
	
@decorators
def div(number1, number2):
	return  number1 // number2

number1 =int(input("Enter the first number: "))
number2 =int(input("Enter the second number: "))
print(number1,number2)


print("The result is: ",div(number1, number2))