'''
Name: Yusuf Halim
File: concentricSquares.py
Class: CS:1210: CS I Fundementals
HW 07: Concentric Squares
Last Date Modified: 06/26/2022
Describtion: draw 10 concetric squares
'''
import turtle

def makeNewTurtle():
    turtle.setup(600, 600)
    window = turtle.Screen()
    window.title('Concentric Squares')
    window.colormode(255)
    
    return turtle.Turtle()

def drawSquare(tur, length):
    '''A function to draw a square'''
    tur.forward(length)
    tur.right(90)
    
    tur.forward(length)
    tur.right(90)
    
    tur.forward(length)
    tur.right(90)
    
    tur.forward(length)
    tur.right(90) 

def main():
    
    square = makeNewTurtle()
    sideLength = 300
    coordinates = sideLength/2
    color = 255
    square.speed(0)
    
    #A loop for drawing the 10 squares
    for i in range(10):
        square.pu()
        square.goto(-coordinates, coordinates)
        square.pd()
        square.color(0, color, color)
        square.begin_fill()
        drawSquare(square, sideLength)
        square.end_fill()
        coordinates -= 15
        sideLength -= 30
        color -= 25
       
    square.ht()
    turtle.done() 
   
main()