
#Funtion accepts Parameters and call another funtion from it

def Add(A,B):
    return A+B

def Sub(A,B):
    return A-B

def Marvellous(Value1,Value2):
    Ans =Add(Value1,Value2)
    print("Addition:",Ans)
    Ans =Sub(Value1,Value2)
    print("Substraction:",Ans)
    
   
     
def main():
    Marvellous(11,6)


if __name__=="__main__":
    main()