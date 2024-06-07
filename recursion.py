# def fact(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n*fact(n-1)
       
# fac=fact(5)    
# print(fac)   
def fibbo():
    n=int(input("enter any no :"))

    a=0
    b=1
    print(a,"\n",b)
    for i in range(1,n+1):
      c=a+b
      a=b
      b=c
      print(c)


fibbo()      