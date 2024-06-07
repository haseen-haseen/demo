# # # class Person:
# # #     cmpnyname="king"
# # #     # def __init__(self):
       
# # #     #     print(f"the name of person is {self.name} and comapnay is {self.cmpnyname}")
# # #     def printname(self):
# # #         print(f"the name of person inside printname is {self.name} and company is {self.cmpnyname}")

# # #     @classmethod   
# # #     def clsmehtod(self,newcmpny):
# # #         self.cmpnyname=newcmpny   




# # # p=Person()
# # # p.name="pagla"
# # # p.printname()
# # # p.clsmehtod("tata")
# # # p.printname()
# # # print(Person.cmpnyname)
# # # print(help(Person))

# # # x=[1,2,3,4]
# # # print(help(Person))
# # class pclass:
# #     print("here is outside code")
# #     def pmethod(self):
# #         print("here is parent method")



# # class sclass(pclass):
# #       def sclass(self):
# #                print("here is sub class method")
               
# #                super().pmethod()



# # sc=sclass()     
# # sc.sclass()     
# # sc.pmethod()     
 
# from typing import Any


# class lenth:
#     name="Rohan"
#     def __len__(self):
#         i=0
#         for c in self.name:
#             # print(self.name)
#            i=i+1
#         return i
#     def __str__(self):
#         return f"your name is {self.name}"
#     def __repr__(self) :
#         return f"you are running the repr method {self.name}"
#     def __call__(self):
#         print (f"heyy how are you")


# ln=lenth()   
# print(ln.name)    
# print(len(ln))     
# # print(str(ln))
# # print(repr(ln))
# ln()



#####        overriding
class rect:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def area(self):
        return self.x*self.y    
class circle(rect):
       def __init__(self,r):
            self.r=r
            super().__init__(r,r)    
       def area(self):
            return 3.14*self.r*self.r   
        



# r=rect(2,3)    
# print(r.area())
cr=circle(5)
print(cr.area())
        