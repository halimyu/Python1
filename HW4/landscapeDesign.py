'''
Name: Yusuf Halim
File: landscapeDesign.py
Class: CS:1210: CS I Fundementals
HW 04: Landscape Design
Last Date Modified: 06/16/2022
Describtion: Calculates sidewalk and garden areas
'''
def main():
    
    base = int(input('How long is the garden: '))
    width = int(input('How wide is the garden: '))
    sidewalkWidth= int(input('How wide are the sidewalks: '))
    
    #formula to get the garden area
    gardenArea = (base-4*sidewalkWidth)*(width-3*sidewalkWidth)
    #formula to get the sidewalk area
    sidewalkArea = (base*width)-gardenArea
    
    print(f'\nArea of the grass is: {gardenArea}',
          f'\nArea of the concrete is: {sidewalkArea}')
    
main()