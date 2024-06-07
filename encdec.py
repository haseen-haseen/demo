
s=str(input("enter any string that u want to encrypt : "))
# isenc=False
option=int(input("enter 1 for encryption"))
words=s.split()
# print(words)
pre="abc"
post="efg"
if(option==1):
    for word in words:
       if(len(word)>3):
          newstring=pre+word[1:]+word[0]+post
          print(newstring)
    else:
          new=s[::-1]   
          print(new)
else:
 if(len(s)>3):
    newstring=s[3:-3]
    newstring=newstring[-1]+newstring[0:-1]
    print(newstring)







   



   
