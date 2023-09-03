
class Arithmatic:
  def  __init__(self,A,B):
    self.No1 =A
    self.No2 =B

  def Accept(self):
        self.No1 =int(input("Enter first number:"))
        self.No2 = int(input("Enter Second number:"))

  def Addition(self):
    Ans =0
    Ans =self.No1+ self.No2
    return Ans

  def Substraction(self):
     Ans =0
     Ans =self.No1 - self.No2
     return Ans
  
  def Multiplication(self):
     Ans =0
     Ans =self.No1 * self.No2
     return Ans
  
  def Division(self):
     Ans =0
     Ans =self.No1 / self.No2
     return Ans

def main():
    
    
    arithmatic = Arithmatic(0,0)
    arithmatic.Accept()
    add= arithmatic.Addition()
    sub =arithmatic.Substraction()
    mul= arithmatic.Multiplication()
    div= arithmatic.Division()

    print(f"Addition is: {add}")
    print(f"Substraction is: {sub:.2f}")
    print(f"Multiplication is: {mul:.2f}")
    print(f"Div is: {div:.2f}")
    
if __name__=="__main__":
    main()