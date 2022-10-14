'''
Name: Yusuf Halim
File: cableRevenue.py
Class: CS:1210: CS I Fundementals
HW 02: Cable Installation Revenue
Last Date Modified: 06/16/2022
Discribtion: Calculates total revenue from cable installation
'''
def main():
    
    yards = int(input('Yards of cable: '))
    location = int(input('Number of locations: '))
    
    
    #Equation to get the total revenue from cable installation 
    #3 is to convert from yards to feet, 2 is the charge per foot 
    #25 is main cost for installation per location
    revenue = 25*location + 3*2*yards
    
    print(f'\nThe revenue generated from {yards} yards of cable \nat',
          f'{location} different locations is ${revenue}')
    
main()