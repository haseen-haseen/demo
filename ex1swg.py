import random
# print(random.randint(0,2))
# 1 snake , 2 water , 3 gun 
#user 1 comp -1
def winner(comp,user):
    if(comp==user):
        return 
    elif(comp==3 and user==1) or (comp==1 and user==2) or (comp==2 and user==3):
        return -1
    else:
        return  1



comp=random.randint(1,3)
user=int(input("enter input from the below options :   \n For Snake 1  \n For Water 2  \n For Gun 3  \n user enter value :  "))
result= winner(comp,user)
if(result==1):
    print("user win")
elif(result==-1):
    print("computer win") 
else:
    print("its a tie ")       
print(f"computer input is : {comp}")
print(f"your input :{user}")

