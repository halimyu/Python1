'''
Name: Yusuf Halim
File: fourCircles.py
Class: CS:1210: CS I Fundementals
HW 08: Four Circles
Last Date Modified: 06/26/2022
Describtion: draw 4 tangent circles
'''
import turtle

def makeNewTurtle():
    turtle.setup(500, 500)
    window = turtle.Screen()
    window.title('Four Circles')
    window.bgcolor('light blue')
    
    return turtle.Turtle()  
    

def main():
    
    circle = makeNewTurtle()
    
    radius = turtle.numinput('Enter Radius', 'Enter Radius')
    
    coordinates = radius
    circle.pu()
    circle.goto(coordinates, 0)
    circle.pd()
    for i in range(2):
        for i in range(2):
            circle.circle(radius)
            circle.pu()
            circle.goto(coordinates, -radius*2)
            circle.pd()
            
        coordinates = -radius
        circle.pu()    
        circle.goto(coordinates, 0)
        circle.pd()
        
       
    circle.ht()
    turtle.done() 
   
main()
