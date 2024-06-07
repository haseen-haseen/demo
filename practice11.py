class c2dvec:
    def __init__(self,i,j) :
        self.i=i
        self.j=j
    def __str__(self) :
        return(f"{self.i}i + {self.j}j ")  
class c3dvec(c2dvec):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k
    def __str__(self):
        return(f"{self.i}i + {self.j}j + {self.k}k")  


c2d=c2dvec(1,2)
c3d=c3dvec(1,2,3)
print(c2d)
print(c3d)

