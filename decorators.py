def addgreet(fn):
 def rfun(*larg,**Darg):
    print("good morning")
    fn(*larg,**Darg)
    print("thanks for using have a good day")
 return rfun  

# @addgreet
# def hello():
#     print("hello world")
@addgreet
def add(a,b):
    print(a+b)
add(5,6)    
# hello()    