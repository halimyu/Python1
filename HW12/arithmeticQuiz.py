'''
Name: Yusuf Halim
File: arithmeticQuiz.py
Class: CS:1210: CS I Fundementals
HW 12: Arithmetic Quiz
Last Date Modified: 07/02/2022
Describtion: gives an arthimitic quiz with random numbers and operators
'''
import random

def main():
    
    operators = ['+','-','*']
    correctAns = 5
    
    for i in range(5):
        operate = random.choice(operators)
        number1 = random.randint(1,9)
        number2 = random.randint(1,9)        
        userAnswer = int(input(f'{number1} {operate} {number2} = '))
        correctAnswer = eval(str(number1) + operate + str(number2))
        if not userAnswer == correctAnswer:
            print(f'   Sorry, {number1} {operate} {number2} = {correctAnswer}')
            correctAns -= 1
        
    
    print(f'You got {correctAns} out 5 correct')
    
main()