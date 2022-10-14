'''
Name: Yusuf Halim
File: passwordValidator.py
Class: CS:1210: CS I Fundementals
HW 15: password Validator
Last Date Modified: 07/04/2022
Describtion: check if password is valid or not
'''

import string

def validPassword(password):
    
    lower = string.ascii_lowercase
    upper = lower.upper()
    digit = string.digits
    special = '~`!@#$%^&*()_-+={}[]<>;:,.?'
    
    specialCh = False
    upperCase = False
    lowerCase = False
    digits = False
    
    validCharachters = lower+upper+digit+special
    
    if not len(password) >= 12:
        return False
    else:
        for ch in password:
            if ch not in validCharachters:
                return False
            elif ch in lower:
                lowerCase = True
            elif ch in upper:
                upperCase = True
            elif ch in digit:
                digits = True
            elif ch in special:
                specialCh = True
                
    if specialCh & upperCase & lowerCase & digits:
        return True
    else:
        return False

            
    