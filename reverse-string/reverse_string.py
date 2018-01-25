def reverse(mydata):
    revstr=""
    for i in mydata:
       revstr=i+revstr
    return revstr
    
reverse(raw_input('Enter String :'))