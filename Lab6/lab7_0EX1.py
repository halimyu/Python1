'''
Name: Yusuf Halim
File: lab7_0EX1.py
Class: CS:1210: CS I Fundementals
Lab 07: Flatten a List Recursively
Last Date Modified: 07/28/2022
Describtion: flattning a list recursively
'''
def flatten(obj):
    if S == []:
        return S
    if isinstance(S[0], list):
        return flatten(S[0]) + flatten(S[1:])
    return S[:1] + flatten(S[1:])