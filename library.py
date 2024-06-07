# class Library:

#     # def __init__(self,no_book,Books):
#     #     self.no_book=no_book
#     #     self.Books=Books

#     def lenofbook(self,list):
        
#         length=len(list)    
#         print(length)
#         return length

#     def addbook(self,abook,list):
#         list.append(abook)
#         return list
        
        
# b=Library()   
# list=["a","b","c"]
# print(b.addbook("newbook2",list) )
# b.lenofbook(list)   

class library:
    def __init__(self) :
        self.booklist=[]

    def addbook(self,newbook):
        return self.booklist.append(newbook)
        
    def showbook(self):
        length=len(self.booklist)  
        print(f"The no of books are {length} and the list of books are : " )
        for book in self.booklist:
            print(book)
       
        
l=library()
l.addbook("book1")
l.addbook("book2")
l.showbook()


        
