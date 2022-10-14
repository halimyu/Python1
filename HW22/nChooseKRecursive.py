'''
Name: Yusuf Halim
File: nChooseKRecursive.py
Class: CS:1210: CS I Fundementals
HW 22: n Choose k Recursive
Last Date Modified: 07/24/2022
Describtion: computes (n k) using recursion
'''
def nChooseK(n, k):
   
   
      if n == 0 or k == 0 or n == k:
            return 1
      else:
            return nChooseK(n-1, k-1) + nChooseK(n-1, k)
   
    
