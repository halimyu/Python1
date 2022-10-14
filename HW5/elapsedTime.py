'''
Name: Yusuf Halim
File: elapsedTime.py
Class: CS:1210: CS I Fundementals
HW 05: Elapsed Time
Last Date Modified: 06/18/2022
Describtion: Calculates elapsed time
'''
def main():
   
    print('Time 1:')
    hour1 = int(input('\tEnter hour: '))
    minute1 = int(input('\tEnter minute: '))
    second1= int(input('\tEnter Second: '))
    
    print('\nTime 2:')
    hour2 = int(input('\tEnter hour: '))
    minute2 = int(input('\tEnter minute: '))
    second2= int(input('\tEnter Second: ')) 
    
    timeTotal1 = (hour1*60*60)+(minute1*60)+second1
    timeTotal2 = (hour2*60*60)+(minute2*60)+second2
    elapsedTime = timeTotal2-timeTotal1
    
    elapsedHour = int(elapsedTime/60/60)
    elapsedMinute = int((elapsedTime-(elapsedHour*60*60))/60)
    elapsedSecond = int((elapsedTime-(elapsedHour*60*60))-elapsedMinute*60)
    
    print('\nElapsed Time:')
    print(f'\t{elapsedHour} hours \n\t{elapsedMinute} minutes',
          f'\n\t{elapsedSecond} seconds')
    
    
main()