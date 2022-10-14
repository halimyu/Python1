'''
Name: Yusuf Halim
File: fibonacciOrder.py
Class: CS:1210: CS I Fundementals
HW 17: nth Order Fibonacci Sequence
Last Date Modified: 07/15/2022
Describtion: gets the the kth term in a fibonaci sequence of order n
'''
def fibonacciOrder(N, K):
    
    fibonacciList = [1]
    
    fibonacci = 0
    if K == 0:
        return fibonacciList[0]
    elif (K >= 2 and K <= N):
        for i in range(1, K):
            for j in range(0, i):
                fibonacci += fibonacciList[j]
            fibonacciList.append(fibonacci)
            fibonacci = 0            
    else:
        for i in range(1, N):
            for j in range(0, i):
                fibonacci += fibonacciList[j]
            fibonacciList.append(fibonacci)
            fibonacci = 0 
            
        for i in range(N, K):
            for j in range(i-N, i):
                fibonacci += fibonacciList[j]
            fibonacciList.append(fibonacci)
            fibonacci = 0
            
        
    return fibonacciList[K-1]
     
