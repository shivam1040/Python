class Library:
    
    def __init__(self, booklist):
        self.booklist=booklist
    
    def dispavailabook(self):
        for book in self.booklist:
            print(book+" ")
    
    def borrow(self, bookbor):
        if bookbor in self.booklist:
            print("borrowed")
            self.booklist.remove(bookbor)
        else:
            print("NA")
    
    def returnbo(self, bookr):
        self.booklist.append(bookr)
        print("returned")
    
class Stud:
    
    def reqbook(self):
        self.bok=input("enter book name: ")
        return self.bok

    def retbok(self):
        self.bok=input("enter bok2: ")
        return self.bok

if __name__=="__main__":
    
    libo=Library(["A", "B", "C"])
    stud1=Stud()
    libo.dispavailabook()
    
    while(True):
        a=int(input("enter choice: "))
        if a==1:
            libo.dispavailabook()
        elif a==2:
            libo.borrow(stud1.reqbook())     
        elif a==3:
            libo.returnbo(stud1.retbok())
        elif a==4:
            exit()
        else:
            print("Invalid")

#if book in listbook: this can be used to find a string in list
#print "NA"
