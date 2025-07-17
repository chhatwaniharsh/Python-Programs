class Book:
    def __init__(self,i,n,a,p,pr):
        self.bid=i
        self.name=n
        self.author=a
        self.publisher=p
        self.price=pr
    def __str__(self):
        return f"Book ID={self.bid}, Book Name={self.name}, Book Author={self.author}, Book Publisher={self.publisher}, Book Price={self.price}"

b1=Book(1,"ABC","DEF","GHI",850)
b2=Book(2,"JKL","MNO","PQR",480)
book_list=[b1,b2]
for books in book_list:
    print(books)
