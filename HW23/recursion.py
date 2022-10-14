'''
Name: Yusuf Halim
File: recursion.py
Class: CS:1210: CS I Fundementals
HW 23: Three Recursive Problems
Last Date Modified: 07/30/2022
Describtion: three programs that removes substrings from a string, get's two 
closer numbers, and longest length of substring in a string
'''
deff = -1
num1 = 0
num2 = 0
def removeSubstrings(message, subString):
    if len(message) == 0:
        return ''
    if len(subString) == 0:
            return message    
    if message.startswith(subString):
        return removeSubstrings(message[len(subString):], subString)
    else:
        return message[0] + removeSubstrings(message[1:], subString)
    
def closest(List):
    global deff, num1, num2
    deff1 = -1
    if deff == -1:
        deff = max(List) - min(List)
        deff1 = max(List) - min(List)
    if len(List) == 1:
        deff = -1
        return [num1, num2]
    if abs(List[0] - List[1]) <= deff:
        deff = abs(List[0] - List[1])
        num1 = List[0]
        num2 = List[1]
    return closest(List[1:])

def strDist(message, substr):
    if len(message) < len(substr):
        return 0
    if message.startswith(substr) and message.endswith(substr):
        return len(message)
    return max(strDist(message[1:], substr), strDist(message[:-1], substr))