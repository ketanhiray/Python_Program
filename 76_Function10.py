
# Function define another funtion inside it (Inner funtion)
# abstraction
def Marvellous(Value1,Value2): # wrapper funtion
    def Add(A,B):
        return A+B 
    
    Ans =Add(Value1,Value2)
    return Ans


def main():
    Ret= Marvellous(11,7)
    
    print("Addition is:",Ret)


if __name__=="__main__":
    main()