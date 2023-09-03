class Numbers:
    def __init__(self,value):
        self.Value =value

    def ChkPrime(self):
        if self.Value <=1:
            return False
        if self.Value==2:
            return True
        if self.Value % 2 ==0:
            return False
        for i in range(3,int(self.Value ** 0.5) +1,2):
            if self.Value % i == 0:
                return False
        return True
    
    def Factors(self):
        factors =[]
        for i in range(1,self.Value +1):
            if self.Value % i == 0:
                factors.append(i)
        return factors
    
    def SumFactors(self):
        factor =self.Factors()
        return sum(factor)
    
    def chkPerfect(self):
        return self.SumFactors() == 2 * self.Value
    
No1= Numbers(int(input("Enter the Number:")))
No2= Numbers(int(input("Enter the Number:")))

print("**************************************")
print("No1:",No1.Value)
print("It is Prime Number?:",No1.ChkPrime())
print("It is Perfect Number?:",No1.chkPerfect())
print("Factors of Number:",No1.Factors())
print("Sum of Factors:",No1.SumFactors())
print("**************************************")



print("**************************************")
print("No2:",No2.Value)
print("It is Prime Number?:",No2.ChkPrime())
print("It is Perfect Number?:",No2.chkPerfect())
print("Factors of Number:",No2.Factors())
print("Sum of Factors:",No2.SumFactors())
print("**************************************")