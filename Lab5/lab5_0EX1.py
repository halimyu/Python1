'''
Name: Yusuf Halim
File: lab5_0EX1.py
Class: CS:1210: CS I Fundementals
Lab 05: Sum of all numbers
Last Date Modified: 07/14/2022
Describtion: takes only ints outside of a List and then sum the numbers together
'''

def sumIntegers(L):
    
    sumOfInt = 0
    
    for item in L:
        if type (item) == type(sumOfInt):
            sumOfInt += item
        
    
    return sumOfInt
        