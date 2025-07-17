class Book:
    def assign(self,i,n,a,p):
        self.bid=i
        self.name=n
        self.author=a
        self.price=p
    def disp(self):
        print(f"Book ID : {self.bid}")
        print(f"Book Name : {self.name}")
        print(f"Book Author : {self.author}")
        print(f"Book Price : {self.price}")

b1=Book()
b2=Book()

b1.assign(1,"ABC","DEF",245)
b2.assign(2,"GHI","JKL",430)

book_list=[b1,b2]
for i in book_list:
    i.disp()
    print()
