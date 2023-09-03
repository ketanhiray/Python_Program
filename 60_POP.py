def Addtion(No1,No2):
  Ans =0
  Ans =No1 + No2
  return Ans

def Subsrction(No1,No2):
  Ans =0
  Ans =No1 - No2
  return Ans


def main():
    value1 =int(input("Enter first number:"))
    value2 = int(input("Enter Second number:"))
    
    Ret = Addtion(value1,value2)
    print("Addition is:",Ret)
    
    Ret = Subsrction(value1,value2)
    print("Substraction is:",Ret)



if __name__=="__main__":
    main()