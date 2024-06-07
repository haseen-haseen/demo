# def fun():
#     try:
#        n=int(input("enter any no"))
#        for i in range(11):
#           print(f"{n} X {i} = {n*i}")
#           return 1
#     except :
#        print("here is error")
#        return 0
#     finally:
#        print("i am always with u")    
#     print("end of code") 


# fun()

n=int(input("enter no between 2 to 5"))
if(n<2 or n>5):
   raise ValueError(f"u are enter wrong value {n}")
   
print(n)   


