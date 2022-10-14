'''
Name: Yusuf Halim
File: nChoose2.py
Class: CS:1210: CS I Fundementals
HW 13: Arithmetic Quiz
Last Date Modified: 07/03/2022
Describtion: gives the number of possiblities a term can be selected from (n,2)
'''
def nChoose2(n):
    
    values = n
    accumlator = 0
    for i in range(1, n):
        for j in range(values-1):
            accumlator += 1
        
        values -= 1
    
    return accumlator


