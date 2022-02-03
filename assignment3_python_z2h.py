# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 10:48:32 2022

@author: Suyog
"""

# Python code to find key with Maximum value in Dictionary

# Dictionary Initialization
TV_TRPS = {'DramaSerials':100, 'CricketMatch':1292, 'ComedySerials' : 88, 'HindiMovies': 1210, 'EnglishMovies': 74}

# taking list of car values in v
v = list(TV_TRPS.values())
 
# taking list of car keys in v
k = list(TV_TRPS.keys())
 
print("The maximum TRP for TV channels is from " + k[v.index(max(v))])