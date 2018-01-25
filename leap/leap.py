def is_leap_year(year):
    tmp=year%4 
    if tmp==0:
        tmp1=year%100
        tmp2=year%400
        if tmp1==0 and tmp2==0 :
            print year, 'is leap year'
            return True
        elif tmp1==0:
            print year, 'is not leap year' 
            return False
        else:
            print year, 'is leap year' 
            return True      
     
    else:
     print year, 'is not leap year'
     return False

year=input("What is the Year? ")   
is_leap_year(year)
print year


 
