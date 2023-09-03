
class Arithematic:
  def  __init__(self,A,B):
    print("Inside Constructor")
    self.No1 =A
    self.No2 =B
    
  def Addition(self):
    Ans =0
    Ans =self.No1+ self.No2
    return Ans

  def Substraction(self):
     Ans =0
     Ans =self.No1 - self.No2
     return Ans
    


def main():
    value1 =int(input("Enter first number:"))
    value2 = int(input("Enter Second number:"))
    
    obj1 =Arithematic(value1,value2)

    Ret = obj1.Addition()
    print("Addition is:",Ret)

    value1 =int(input("Enter first number:"))
    value2 = int(input("Enter Second number:"))
    
    obj2 =Arithematic(value1,value2)

    Ret = obj2.Substraction()
    print("Substraction is:",Ret)
    
if __name__=="__main__":
    main()