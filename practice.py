# n= int(input("enter a no :"))    
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print("factorial is ",fact)

# n= int(input("enter a no :"))    
# fact=1
# i=1
# while(i<n+1):
#    fact=fact*i
#    i=i+1
# print("factorial is ",fact)

# n= int(input("enter a no :"))    
# fact=1
# while(n>1):
#    fact=fact*n
#    n=n-1
# print("factorial is ",fact)

# n=int(input("enter no :"))
# if(n%2==0):
#     print("no is even")
# else:
#     print("no is odd")  
  
# n=10
# for i in range(1,n+1):
#     i=i*2-1
#     print(i)
# ---------------odd no------------------  
# n=int(input("enter a no: "))
# i=1
# while(i<=n):
#     b=i*2-1
#     i=i+1
#     print(b)
# --------------------Find the Largest Number in a List:--------------
# list=[1,3,56,3,2,6]
# print(max(list))
# ---------Calculate the Area of a Rectangle:--------------------
# len=int(input("enter length :"))
# brdth=int(input("enter breadth :"))
# area=2*(len+brdth)
# print(area)
# --------fibbo----------
# n= int(input("enter no "))
# a=0
# b=1
# print(a,b)
# i=2
# while(i<=n):
#     c=a+b
#     a=b
#     b=c
#     i=i+1
#     print(c)
# ------------palindrome--------------

# n= int(input("enter any no :"))
# temp=n
# r=0
# while(temp != 0):
#     d=temp % 10
#     r= r * 10 + d
#     temp = temp // 10
# if(r==n):
#     print("no is palindrom")    
# else:
#     print("no is not palindrom")    
# --------------reverse a string-----------------------
# name="shine"
# print(name[::-1])
# ---------------------calculate sum in a number------------------
# n= int(input("enter any no : "))
# sum=0
# temp=n
# while(temp!=0):
#     d=temp%10
#     sum=sum+d
#     temp=temp//10
# print(sum)    
# -------------------check no is prime-----------------------
# n=int(input("enter any no: "))    
# i=2
# # for i in range(2,(n//2)+1):
# while(i<=n/2):
#  if(n%i==0):
#         s=n%i
#         print(s)
#         print("n is not prime")
#         break
#  i=i+1
# else:
#   print(n%i)
#   print("no is prime") 
# -------------------c to f program-------------- 
# c=int(input("enter temprature in C "))
# f=(9/5)*c + 32
# print(f)
# -----------------present or not  vowels in a string----------
# n=str(input("enter any string"))
# for i in n:
#     if(i=='a' or i=='e'or i=='o' or i=='i' or i=='u'):
#         c=n.count(i)
#         print(c)
# n=str(input("enter any string"))
# vowel={'a','e','i','o','u'}
# c=0
# for char in n:
#     if char in vowel:
#         c=c+1
# print(c)
       ## -------------------sum of  natural no.--
# n=int(input("enter range no "))
# sum=0
# for i in range(n+1):
#     sum=sum+i
# print(sum)


