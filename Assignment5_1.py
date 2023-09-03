
class Demo:
  def  __init__(self,A,B):
    print("Inside Constructor")
    self.No1 =A
    self.No2 =B
    
  def Fun(self):
    Ans =0
    Ans =self.No1+ self.No2
    return Ans

  def Gun(self):
     Ans =0
     Ans =self.No1 - self.No2
     return Ans
    


def main():
    value1 =int(input("Enter first number:"))
    value2 = int(input("Enter Second number:"))
    
    obj1 =Demo(value1,value2)
    obj2 =Demo(value1,value2)
    Ret = obj1.Fun()
    print("Value obj1.Fun() of Fun is:",Ret)
    Ret = obj2.Fun()
    print("Value obj2.Fun() of Fun is:",Ret)
    Ret = obj1.Gun()
    print("Value obj1.Gun() of is:",Ret)
    Ret = obj2.Gun()
    print("Value obj2.Gun() of is:",Ret)
    
if __name__=="__main__":
    main()