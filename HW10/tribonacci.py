'''
Name: Yusuf Halim
File: tribonacci.py
Class: CS:1210: CS I Fundementals
HW 10: Tribonacci Sequence
Last Date Modified: 07/02/2022
Describtion: gives the nth term in the tribonacci sequence
'''        
def tribonacci(n):
    
    tribonacciTerm = 0
    
    if (n == 1 or n == 2) :
        tribonacciTerm = 1
    elif (n == 3) :
        tribonacciTerm = 2
    else :
        tribonacciTerm = tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)
    
    
    return tribonacciTerm        
         
