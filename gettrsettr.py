class gttrsttr:
    def __init__(self,value):
        self._value=value
    def show(self):
        print(f"value is {self._value}")    
    @property   
    def value(self):
        return 10*self._value
    @value.setter   
    def valueset(self,newvalue):
        self._value=newvalue/10
        


a=gttrsttr(10)
a.show()
print(a.value)
a.valueset=56
print(a.valueset)