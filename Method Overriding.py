class Calc:
    def div(self,a,b):
        ans=a/b
        print(ans)
class AdvCalc(Calc):
    def div(self,a,b):
        Q=a//b
        R=a%b
        ans=a/b
        print("Q :",Q)
        print("R :",R)
        print("Ans :",ans)
ac=AdvCalc()
ac.div(10,20)
