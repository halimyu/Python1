'''
Name: Yusuf Halim
File: lab7_0EX1.py
Class: CS:1210: CS I Fundementals
Lab 07: Flatten a List Recursively
Last Date Modified: 07/28/2022
Describtion: flattning a list recursively
'''
def flatten(obj):
    if obj == []:
        return obj
    if isinstance(obj[0], list):
        return flatten(obj[0]) + flatten(obj[1:])
    return obj[:1] + flatten(obj[1:])