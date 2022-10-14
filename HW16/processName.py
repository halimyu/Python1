'''
Name: Yusuf Halim
File: processName.py
Class: CS:1210: CS I Fundementals
HW 16: Process Name
Last Date Modified: 07/03/2022
Describtion: Seprate First, Middle, and Last names from a string
'''
def processName(name):
    
    endOfFirst = name.find(' ')
    endOfMiddle = name.rfind(' ')
    
    first = name[0:endOfFirst]
    middle = name[endOfFirst+1:endOfMiddle]
    last = name[endOfMiddle+1:]
    
    return first, middle, last
