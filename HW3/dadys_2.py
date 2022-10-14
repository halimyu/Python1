""""
Test by Yusuf Dad
""""
def main():
    
    x= float(input('inter the legnth: '))
    y= float(input('inter the width: '))
    d=  float(input('inter the side walk: '))
    greenarea=( x-4*d)*(y-3*d)
    sidewalk= x*y-greenarea
    
    print(f'green area :'{greenarea})
    print(f'side walk :'{sidewalk})
    
main()