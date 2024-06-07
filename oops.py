class info:
    def __init__(self,n,a,g) :
        self.name=n
        self.age=a
        self.gender=g
        print(f"{n} is a {g} hvaing age {a}")

    # name="shine"
    # age="19"
    # gender="female"
    def menu(self):
        print(f"{self.name} is a {self.gender} having age {self.age}")


class addinfo(info):
    def newtest(self):
        print("here is your subclass")
        
# a=info("harry","28","male")
a=addinfo("harry","28","male")
# b=info("shruti","18","female")
a.newtest()
# a.menu()


