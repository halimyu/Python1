'''
Name: Yusuf Halim
File: millionaire.py
Class: CS:1210: CS I Fundementals
HW 06: How to Become a Millionaire
Last Date Modified: 06/26/2022
Describtion: Calculates future value after acumlated intrest over the year
'''
import turtle

def createTurtle():
    turtle.setup(450, 450)
    window = turtle.Screen()
    window.title('HW 06 -How to Become a Millionaire')
    
    return turtle.Turtle()

def main():
    
    #call create turtle method and adjust the turtle's position
    cuff = createTurtle()
    cuff.hideturtle()
    cuff.speed(0)
    cuff.pu()
    cuff.goto(0,120)
    
    #ask user for inputs to calculate future value
    monthlyAmount = turtle.numinput('Amount Saved Each Month', 
                                      'Amount saved each month (Pmt)')
    years = turtle.numinput('Number of Years', 'Number of years (n)')
    annualIntrest = turtle.numinput('Annual Interest Rate', 
                                   'Annual interest rate (i)')
    
    #calculates the future value based on the inputes gathered above
    futureValue = monthlyAmount*((((1+annualIntrest/1200)**(12*years))-1)/
                                 (annualIntrest/1200))
    
    #use turtle write method to input the value with formats
    font = ('Arial', 12, 'bold')
    cuff.write(f'Amount at the end (FV): ${futureValue:,.2f}', 
               False, 'center', font)
              
    
    turtle.done()
    
main()

