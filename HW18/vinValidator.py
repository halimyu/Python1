'''
Name: Yusuf Halim
File: vinValidator.py
Class: CS:1210: CS I Fundementals
HW 18: VIN Validator
Last Date Modified: 07/15/2022
Describtion: Check if a car VIN is valid or not using an VIN Checksum Algorithm
'''

def validateVIN(VIN):
    
    NumericChar = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5 , 'F':6, 'G':7, 'H':8, 
                   'J':1, 'K':2, 'L':3, 'M':4, 'N':5, 'P':7, 'R':9, 'S':2, 'T':3
                   , 'U':4, 'V':5, 'W':6, 'X':7, 'Y':8, 'Z':9}
    
    weight = [8, 7, 6, 5, 4, 3, 2, 10, 0, 9, 8, 7, 6, 5, 4, 3, 2]
    
    weightedProduct = 0
    
    if (len(VIN) < 17):
        return False
    elif (len(VIN) > 17):
        return False
    elif (not str.isdigit(VIN[8]) and VIN[8] != 'X'):
        return False
    elif VIN in '1'*17:
        return True    
    
    for item in VIN:
        if item == 'I' or  item == 'O' or item == 'Q':
            return False
        
    
    
    listVIN = list(VIN)
    
    for item in range(0, len(listVIN)):
        if listVIN[item] in NumericChar:
            weightedProduct += NumericChar.get(listVIN[item]) * weight[item]
        else:
            weightedProduct += int(listVIN[item]) * weight[item]
    
    CheckValue = weightedProduct%11
    
    if (listVIN[8] == 'X'):
        if(CheckValue == 10):
            return True
        else:
            return False
    elif(CheckValue == int(listVIN[8])):
        return True
    else:
        return False
            