'''
Name: Yusuf Halim
File: lab5_0EX1.py
Class: CS:1210: CS I Fundementals
Lab 06: Building a Book Index
Last Date Modified: 07/21/2022
Describtion: Making a book index from a terms file
'''
def index(filename):
    inFile = open(filename, 'r')
    
    outFile = open('index.txt', 'w')
    
    index = {}
    for line in inFile:
        page, word = map(str.strip, line.split(':', 1))
        word = word.lower()
        if word not in index:
            index.setdefault(word, []).append(int(page))            
        else:
            if int(page) not in index.get(word):
                index.setdefault(word, []).append(int(page))
                
    indexList = sorted(index)
    sortedIndex = {}
    
    for i in indexList:
        
        sortedIndex[i] = sorted(index.get(i))
        
        
    for item in sortedIndex:
        pageNumbers = ''
        for i in sortedIndex.get(item):
            pageNumbers += str(i) + ', '
        pageNumbers = pageNumbers[:len(pageNumbers)-2]
        outFile.write(item + ', ' + pageNumbers + '\n')
        print(item + ', ' + pageNumbers)

    
def main():
    
    index('terms.txt')
    
main()