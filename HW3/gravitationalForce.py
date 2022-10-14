'''
Name: Yusuf Halim
File: gravitationalForce.py
Class: CS:1210: CS I Fundementals
HW 03: Gravitional Force
Last Date Modified: 06/16/2022
Describtion: Calculates gravitational force between two bodies
'''
def main():
    
    mass1 = float(input('Mass of body 1: '))
    mass2 = float(input('Mass of body 2: '))
    distance = float(input('Distance between the two bodies: '))
    
    # Equation for gravititional force between the two bodies
    force = 6.67e-8*((mass1*mass2)/(distance**2))
    
    print(f'\nForce is {force}')
    
main()