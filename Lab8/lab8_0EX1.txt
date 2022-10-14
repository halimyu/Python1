'''
Name: Yusuf Halim
File: lab8_0EX1.py
Class: CS:1210: CS I Fundementals
Lab 08: Stack Class
Last Date Modified: 08/04/2022
Describtion: create the stack class
'''
class stack:
    def __init__(self, data = None):
        if data == None:
            self.elements = []
        else:    
            self.elements = data

    def push(self, data):
        self.elements.append(data)

    def pop(self):
        return self.elements.pop()
    
    def top(self):
        return self.elements[-1]
    
    def isEmpty(self):
        if len(self.elements) == 0:
            return True
        return False
    
    def __str__(self):
        return f'{self.elements} TOS'
    
    def __repr__(self):
        return self.__str__()
    
    def __len__(self):
        return len(self.elements)   
    
    def __eq__(self, other):
        if isinstance(other, stack):
            if self.elements == other.elements:
                return True
            
        return False
    def __ne__(self, other):
        if isinstance(other, stack):          
            if self.elements != other.elements:
                return True
            
        return False    
    
    