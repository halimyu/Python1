"""
test by dadys 2
"""
def main():
    
    print('Time 1')
    time1hours = int(input("Enter hour: "))
    time1mints = int(input("Enter minutes: "))
    time1secs = int(input("Enter seconds: "))
    
    print('Time 2')
    time2hours = int(input("Enter hour: "))
    time2mints = int(input("Enter minutes: "))
    time2secs = int(input("Enter seconds: "))
    
    
    time1total=time1hours*60*60+time1mints*60+time1secs
    time2total=time2hours*60*60+time2mints*60+time2secs
    elabsetimetotal=time2total-time1total
    
    elabsetimehours = elabsetimetotal// (60*60)
    elabsetimeminits= (elabsetimetotal - elabsetimehours *60*60)//60
    elabsetimesecs = elabsetimetotal-(elabsetimehours*60*60)-(elabsetimeminits
    *60)
    
    print(elabsetimehours)
    print(elabsetimeminits)
    print(elabsetimesecs)
    
main()