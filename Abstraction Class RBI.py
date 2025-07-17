from abc import ABC,abstractmethod

class RBI(ABC):
    def new_guidelines(self):
        print("REPO Rate increased by 0.7%")
        print("3rd party cannot save credit card details")
        print("KYC is mandatory every 2 years")
    @abstractmethod
    def interest_rate(self):
        pass

#obj=RBI()  #TypeError

class HDFC(RBI):
    def interest_rate(self):
        print("Interest rate of HDFC Bank is 3.2%")

class ICICI(RBI):
    def interest_rate(self):
        print("Interest rate of ICICI Bank is 3.8%")

h1=HDFC()
h1.new_guidelines()
h1.interest_rate()

print()

i1=ICICI()
i1.new_guidelines()
i1.interest_rate()
