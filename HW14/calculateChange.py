'''
Name: Yusuf Halim
File: calculateChange.py
Class: CS:1210: CS I Fundementals
HW14:Calculate Change
Last Date Modified: 07/10/2022
Describtion: takes a 2 sentences and outputs the change
'''

import string
def stringToInt(sentence):
    
    position = sentence.find('.')
    
    number = 0
    
    if (sentence[position-2:position-1]) in string.digits:
        number =\
            int(sentence[position-2:position]+sentence[position+1:position+3])
    else:
        number =\
            int(sentence[position-1:position]+sentence[position+1:position+3])
    
    return number

def intToString(number):
    
    money = str(number)
    
    if number > 0:
        money = money.zfill(3)
        money = '$' + money[0:(len(money)//2)] + '.' + money[len(money)//2:4]
    else:
        money = '$0.00'
    
    return money
        
def main():
    
    print('How much is owed?')
    sentence1 = input(' > ')
    
    print('How much was paid?')
    sentence2 = input(' > ')
    
    cost = stringToInt(sentence1)
    paid = stringToInt(sentence2)
    
    print(f'\n  Cost: {intToString(cost)}')
    print(f'  Paid: {intToString(paid)}')
    
    if cost > paid:
        print('Not enough was paid.')
    else:
        change = paid - cost
        print(f'Change: {intToString(change)}')
    
main()


        