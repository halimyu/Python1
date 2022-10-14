'''
Name: Yusuf Halim
File: nChooseK.py
Class: CS:1210: CS I Fundementals
HW 19: n Choose k
Last Date Modified: 07/15/2022
Describtion: computes (n k) using piscals triangle algorithm
'''
from math import factorial

def nChooseK(n, k):
   
   
      if n == 0 or k == 0 or n == k:
            return 1
      else:
            nChoose = []
            for i in range(0,n):
                  rows = []
                  for j in range(0,i+1):
                        rows.append(factorial(i)//(factorial(j)*factorial(i-j)))
                  nChoose.append(rows)            
            value = nChoose[n-1][k-1] + nChoose[n-1][k]
            return value
   
    
