'''
Name: Yusuf Halim
File: babyNames.py
Class: CS:1210: CS I Fundementals
HW 21: Baby Names
Last Date Modified: 07/24/2022
Describtion: get baby names and organize them based on most common and first 
             appearance
'''

def menu(fileName, fromDate, toDate):
    
    print(f'\nCurrent range: {fromDate} - {toDate}')
    print(f'Current output file: {fileName}')
    print(f'   1) Specify date range')
    print(f'   2) Specify output file name')
    print(f'   3) Most populat names')
    print(f'   4) When names first appear')
    print(f'   5) Quit')

def popularNames(fileName, fromDate, toDate):
    
    outfile = open(fileName, 'w')
    
    for year in range(fromDate, toDate+1):
        infile = open(f'names\\yob{year}.txt', 'r')
        maxM = 0
        maxF = 0
        female = {}
        male = {}
        for line in infile:
            if line[line.find(',')+1:line.rfind(',')] == 'F':
                female[line[:line.find(',')]] = int(line[line.rfind(',')+1:])
            elif line[line.find(',')+1:line.rfind(',')] == 'M':
                male[line[:line.find(',')]] = int(line[line.rfind(',')+1:])
                
        infile.close()
        
        maxM = max(male.values())
        maxF = max(female.values())
        
        commonF = []
        commonM = []
        for key in female:
            if female[key] == maxF:
                commonF.append(key)
        
        for key in male:
            if male[key] == maxM:
                commonM.append(key)
                
        commonF.sort()
        commonM.sort()
        
        outfile.write(f'Most popular female names for {year}\n')
        for name in commonF:
            outfile.write(f'{name}\n')
            
        outfile.write(f'\nMost popular male names for {year}\n')   
        for name in commonM:
            outfile.write(f'{name}\n')
        outfile.write('\n')
    
    outfile.close()
    
def firstAppear(fileName, fromDate, toDate):
    
    outfile = open(fileName, 'w')
    apeared = []
    
    for year in range(fromDate, toDate+1):
        infile = open(f'names\\yob{year}.txt', 'r')
        new = []
        for line in infile:
            if line[:line.find(',')] not in apeared:
                new.append(line[:line.find(',')])
                apeared.append(line[:line.find(',')])
        new.sort()
        
        if len(new) > 0:
            outfile.write(f'Names that first apeared in {year}\n')
            for name in new:
                outfile.write(f'{name}\n')
            outfile.write('\n')
        
        infile.close()
    outfile.close()
    

def main():
    
    fromRange = 1880
    toRange = 2018
    end = False
    file = 'output.txt'
    
    while not end:
        menu(file, fromRange, toRange)
    
        selection = int(input('\n   Make selection: '))
    
        if selection == 1:
            fromRange = int(input('\nStarting year: '))
            toRange = int(input('Ending year: '))
            if fromRange < 1880 or fromRange > 2018:
                fromRange = 1880
            elif fromRange > toRange:
                toRange, fromRange = fromRange, toRange
                    
            if toRange > 2018 or toRange < 1880:
                toRange = 2018
            elif toRange < fromRange:
                toRange, fromRange = fromRange, toRange             
        elif selection == 2:
            file = input('\nEnter file name: ')
        elif selection == 3:
            popularNames(file, fromRange, toRange)
            print(f'\nResults written to {file}')
        elif selection == 4:
            firstAppear(file, fromRange, toRange)
            print(f'\nResults written to {file}')
        elif selection == 5:
            end = True        
        else:
            print('Please make a valid selection')
            
    
    
main()
