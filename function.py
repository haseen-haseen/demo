# def add(a,b):
#     sum=a+b
#     print(sum)


# add(1,3)    
# def isgreter(a,b):
#     if(a>b):
#         print("first is greter")
#     else:
#         print("second is greater")

# isgreter(13,5)


# def findmarksper( marks,total):
#     p=marks/total*100
#     print(p)
#     marks=p/100*500
#     print(marks)
# # def findmark(per):
# #     marks=per/100*500
# #     print(marks)
# marks=int(input("enter marks"))
# total=int(input("enter total"))

# findmarksper(marks,total)
# a=int(input("enter per :"))
# findmark(a)

# def avg(*num):
#     sum=0
#     for i in num:
#         sum=sum+i
#     print(sum / len(num))

# avg(5,6)

# def dictonary(**name):
#     print("heyy",name["fname"],name["mname"])

# dictonary(fname="shine",mname="rihan")
sqr=lambda x:x*x
# avg= lambda a,b,c:(a+b+c)/2
# # print(sqr(5))
# # print(avg(2,4,6))
# def jogi(sqr,value):
#     sum=2+sqr(value)
#     return sum

# print(jogi(sqr,2)) 

# lis=[1,2,3,4,6]
# newl=list(map(sqr,lis))
# def ff(a):
#     return a>3
# lln=list(filter(ff,lis))

# newl=[]
# for i in list:
#     newl.append(sqr(i))
# print(newl)
# print(lln)
from functools import reduce
lis=[1,2,3,4,6]
sum=reduce(lambda a,b:a+b,lis)
print(sum)

