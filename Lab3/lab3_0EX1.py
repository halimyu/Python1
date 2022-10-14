'''
Name: Yusuf Halim
File: lab3_0EX1.py
Class: CS:1210: CS I Fundementals
Lab 3-0EX1: Pi Approximation
Last Date Modified: 06/30/2022
Describtion: Approximates the value of pi
'''
import math
def piapprox(n):
    
    piApprox = 0
    
    for i in range(1, n+1, 1):
        term = (1/i**2)
        piApprox += term
        
    piApprox = math.sqrt(6*piApprox)
        
    return piApprox

def main():
    
    terms = int(input('How many terms do you want to test: '))
    approx = piapprox(terms)
    print(approx)
    
main()
    
    
    