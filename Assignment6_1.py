class BookStore:
    NoOfBooks =0  # clas variable

    def __init__(self,Name,Author): # constructor
        self.BookName =Name
        self.BookAurthor =Author  # instance varible
        BookStore.NoOfBooks += 1 


    def DisplayBookinfo(self): # instance mehtod
        print("Book Name:",self.BookName)
        print("Book Author:",self.BookAurthor)
        print("Number of books:",BookStore.NoOfBooks)

def main():
    
 Obj1 = BookStore("Linux System Programming", "Robert Love")
 Obj1.DisplayBookinfo()   
 Obj2 = BookStore("C Programming", "Dennis Ritchie")
 Obj2.DisplayBookinfo()   

if __name__=="__main__":
    main()