'''
Name: Yusuf Halim
File: bullseye.py
Class: CS:1210: CS I Fundementals
HW 08: bullseye
Last Date Modified: 06/26/2022
Describtion: make a bullseye by drawing 12 concentric circles
'''
import turtle

def makeNewTurtle():
    turtle.setup(600, 600)
    window = turtle.Screen()
    window.title('Bullseye')
    window.bgcolor('gray')
    
    return turtle.Turtle()
        

def makeCircle(tur, rad, pen, fill):
    '''A function to draw a circle'''
    tur.pencolor(pen)
    tur.fillcolor(fill)              
    tur.pu()
    tur.sety(-rad)
    tur.pd()          
    tur.begin_fill()
    tur.circle(rad)
    tur.end_fill()    
    

def main():
    
    circle = makeNewTurtle()
    radius = 240
    circle.speed(0)
    penColor = 'black'
    fillColor = 'white'
    
    #draw white and black circle
    for i in range(2):
        for j in range(2):
            makeCircle(circle, radius, penColor, fillColor)
            radius -= 23
        penColor = 'white'
        fillColor = 'black'
    
    #draw cyan and red circle
    penColor = 'black'
    fillColor = 'cyan'
    for i in range(2):
        for j in range(2):
            makeCircle(circle, radius, penColor, fillColor)
            radius -= 23
        fillColor = 'red'  
        
    #draw yellow circle
    for i in range(1):
        fillColor = 'yellow'
        for j in range(2):
            makeCircle(circle, radius, penColor, fillColor)
            radius -= 19
        
        penColor = 'gray'    
        makeCircle(circle, radius, penColor, fillColor)
        radius -= 19
        
    #draw a dot
    fillColor = 'black'
    penColor = 'black'
    makeCircle(circle, radius, penColor, fillColor)
       
    circle.ht()
    turtle.done() 
   
main()
