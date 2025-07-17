class Bank:
    name="Shiv"
    amount=29000
    def deposit(self,a):
        self.a=a
        self.amount+=self.a
        print("Total Amount after Deposit:",self.amount)
    def withdraw(self,a):
        self.a=a
        self.amount-=self.a
        print("Total Amount after Withdraw:",self.amount)
    def getData(self):
        print("Name :",self.name)
        print("Total Amount :",self.amount)
b1=Bank()
b1.getData()
b1.deposit(12000)
b1.withdraw(8500)
b1.getData()
    
    
