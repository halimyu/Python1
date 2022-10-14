'''
Name: Yusuf Halim
File: mySet.py
Class: CS:1210: CS I Fundementals
HW 24: mySet Class
Last Date Modified: 08/05/2022
Describtion: creating a set class clone
'''
class mySet:
    def __init__(self, data = None):
        if data == None:
            self.__elements = []
        else:
            self.__elements = []
            if len(data) > 0:
                for i in data:
                    if i not in self.__elements:
                        self.__elements.append(i)
                        
            self.__elements = sorted(self.__elements)

    def add(self, data):
        if data not in self.__elements:
            self.__elements.append(data)
    
        self.__elements = sorted(self.__elements)        

    def pop(self):
        if len(self.__elements) > 0:
            return self.__elements.pop()
        raise KeyError('empty set!')
    
    def remove(self, key):
        if key in self.__elements:
            self.__elements.remove(key)
        else:
            raise KeyError('This value was not found in the set') 
    
    def discard(self, key):
        if key in self.__elements:
            self.__elements.remove(key)    
    
    def clear(self):
        if len(self.__elements) > 0:
            self.__elements.clear()
    
    def copy(self):
        from copy import copy
        return copy(self)
    
    def issubset(self, otherSet):
        return self.__le__(otherSet)
    
    def ispropersubset(self, otherSet):
        return self.__lt__(otherSet)
    
    def issuperset(self, otherSet):
        return self.__ge__(otherSet)
    
    def ispropersuperset(self, otherSet):
        return self.__gt__(otherSet)    
    
    def union(self, otherSet):
        return self.__or__(otherSet) 
    
    def intersection(self, otherSet):
        return self.__and__(otherSet)
    
    def difference(self, otherSet):
        return self.__sub__(otherSet)
    
    def symmetric_difference(self, otherSet):
        return self.__xor__(otherSet)
    
    def isdisjoint(self, otherSet):
        if len(self.intersection(otherSet)) == 0:
            return True
        return False
    
    def update(self, otherSet):
        self.__ior__(otherSet)
        
    def intersection_update(self, otherSet):
        self.__iand__(otherSet)
    
    def difference_update(self, otherSet):
        self.__isub__(otherSet)
    
    def symmetric_difference_update(self, otherSet):
        self.__ixor__(otherSet)
    
    def __str__(self):
        return f'{self.__elements}'
    
    def __repr__(self):
        return self.__str__()
    
    def __len__(self):
        return len(self.__elements)   
    
    def __contains__(self, key):
        if key in self.__elements:
            return True
        return False
    
    def __eq__(self, other):
        if isinstance(other, mySet):
            if self.__elements == other.__elements:
                return True
            return False
        return False
    
    def __ne__(self, other):
        if isinstance(other, mySet):
            if self.__elements != other.__elements:
                return True
            return False
        return False    
    
    def __le__(self, other):
        if isinstance(other, mySet):
            if self.__elements <= other.__elements:
                return True
            return False
        return False
    
    def __lt__(self, other):
        if isinstance(other, mySet):
            if self.__le__(other) and self.__ne__(other):
                return True
            return False
        return False
    
    def __ge__(self, other):
        if isinstance(other, mySet):
            if self.__elements >= other.__elements:
                return True
            return False
        return False    
    
    def __gt__(self, other):
        if isinstance(other, mySet):
            if self.__ge__(other) and self.__ne__(other):
                return True
            return False
        return False    
    
    def __or__(self, other):
        if isinstance(other, mySet):
            result = mySet(self.__elements)
            for i in other.__elements:
                result.add(i)
            return result
    
    def __and__(self, other):
        if isinstance(other, mySet):
            result = mySet()
            for i in self.__elements:
                if i in other.__elements:
                    result.add(i)
            return result
    
    def __sub__(self, other):
        if isinstance(other, mySet):
            result = mySet()
            for i in self.__elements:
                if i not in other.__elements:
                    result.add(i)
            return result    
            
    def __xor__(self, other):
        if isinstance(other, mySet):
            result = mySet()
            for i in other.__elements:
                if i not in self.__elements:
                    result.add(i)
            for j in self.__elements:
                if j not in other.__elements:
                    result.add(j)
            return result
        
    def __ior__(self, other):
        for i in other.__elements:
            self.add(i)
    
    def __iand__(self, other):
        result = self.__and__(other)
        self.__elements = result
        
    def __isub__(self, other):
        result = self.__sub__(other)
        self.__elements = result
    
    def __ixor__(self, other):
        result = self.__xor__(other)
        self.__elements = result
    
    