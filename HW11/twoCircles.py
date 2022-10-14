'''
Name: Yusuf Halim
File: twoCircles.py
Class: CS:1210: CS I Fundementals
HW 11: Two Circles
Last Date Modified: 07/02/2022
Describtion: determine if circles are inside, outside, or overlaped
'''
import math
def circleOverlab(x1, x2, y1, y2, r1, r2):
    
    case = ''
    if (math.dist((x1,y1), (x2,y2))) > (r1+r2):
        case = 'Small circle is OUTSIDE big circle' 
    
    elif r1>r2:
        if ((x2-x1)**2+(y2-y1)**2) < r1*r1:
            case = 'Small circle is INSIDE big circle'
        else:
            case = 'circles OVERLAP'
    else:
        if ((x1-x2)**2+(y1-y2)**2) < r2*r2:
            case = 'Small circle is INSIDE big circle'
        
        else:
            case = 'circles OVERLAP'        
        
    return case

def main():
    
    print('Circle 1 - Center is (x1, y1), radius is r1')
    x1 = int(input('Enter x1: '))
    y1 = int(input('Enter y1: '))
    r1 = int(input('Enter r1: '))
    
    print('\nCircle 2 - Center is (x2, y2), radius is r2')
    x2 = int(input('Enter x2: '))
    y2 = int(input('Enter y2: '))
    r2 = int(input('Enter r2: '))
    
    case = circleOverlab(x1,x2,y1,y2,r1,r2)
    
    print(f'\n{case}')
    
main()