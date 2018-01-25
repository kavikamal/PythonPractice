def is_isogram(strdata):
    
    for i in strdata :
       if (i != " " and i !="-"):
         countval=strdata.lower().count(i)
         if (countval>1) :
          print strdata ,"is not Isogram"
          return False
       countval=0
    print strdata, "is a Isogram"
    return True
       

is_isogram(raw_input('Enter String :'))