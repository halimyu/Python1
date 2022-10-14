from nChoose2 import *
def main():
    
    errors = False
    tests = [(0,0), (1,0), (2,1), (3,3), (4,6), (10,45), (100,4950)]
    for n, expected in tests:
        answer = nChoose2(n)
        if answer != expected:
            print(f'ERROR: {n} choose 2 = {expected}. Your function returned {answer}')
            errors = True
            
    if not errors:
        print('No errors found')
         
        print(f'dsgsfgf \newline ghehgfdhh')
        print('dsgsfgfghehgfdhh')
        
    
    
    
main()



'''
this was another way that I found also works and shorter
def nChoose2(n):
    
    numWays = 0
    for i in range(1, n):
        numWays += n-i
    
    return numWays
'''
