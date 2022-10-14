'''
Name: Yusuf Halim
file: lab1_0EX1.py
Class: CS:1210: CS I Fundementals
lap01: Driving Calculation, Speed
Date last modified: 06/16/2022
Calculates the speed needed to travel an amount of miles in a period of time.
'''

def main():
    
    miles = int(input('How far do you want to drive: '))
    hours = int(input('How many hours do you want to drive: '))
    
    speed = miles/hours
    
    print(f'\nTo drive {miles} miles in {hours} hours,', 
          f'\nyou need to average at least {speed} MBH')
    
main()