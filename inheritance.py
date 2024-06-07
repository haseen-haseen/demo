# #####----------------Single Inheritance----------------
# # class Animal:
# #     def sound(self):
# #         print("sound of animal are diffrent")

# # class Dog(Animal):
# #     def sound(self):
# #         print("BArking....")   



# # D =Dog()
# # D.sound()   
# # A=Animal()
# # A.sound()    

# ##############--------------Multiple Inheritance--------------
# # class Mother:
# #     Mname=""
# #     def Mothername(self):
# #         print(f"MotherName: {self.Mname}")    

# # class Father:
# #     FatherName=""

# #     def Fathername(self):
# #         print(f"FatherName: {self.FatherName}")    

# # class Son(Father,Mother):
# #     def  sonname(self,name):
# #         self.name=name
# #         print(f"Son : {self.name} \n Father: {self.FatherName} \n Mother: {self.Mname}")


# # S=Son()  
# # S.name="Rihan" 
# # S.FatherName="Riyaz"
# # S.Mname="Riza"
# # S.sonname(S.name)
# # print(Son.mro())


# class employee:
#     def __init__(self,name) :
#         self.name=name
#     def dnem(self):
#         print(f" dancer name is {self.name}")    

# class dancer:
#     def __init__(self,dancer):
#         self.dancer=dancer
#     def dnem(self):
#         print(f" dance is {self.dancer}")

# class empdnc(dancer,employee) :
#     def __init__(self,name,dancer):  
#         self.name=name
#         self.dancer=dancer
#     def emdn(self):
#         print(f"{self.name} {self.dancer}")



# ed=empdnc("shivani","kathak")
# ed.emdn()
# ed.dnem()
# # print(ed)     

##################----------------------Multilevel   Inheritance 

# class Grandfather:
#     def gfh(self):
#         print("i am grandfather")

# class Father(Grandfather):
#     def fh(self):
#         print("i am father")    
# class son(Father):
#     def sn(self):
#         print(" i am grandson of gfh and son of fh")        


# s=son()
# s.sn() 
# s.fh()
# s.gfh()           


    
     
        
         
                
        

                    
        
    