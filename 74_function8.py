
#Funtion accepts Parameters and call another funtion from it and return multiple values
# using lambada funtion

Add = lambda A,B :A+B
Sub = lambda A,B :A-B

def Marvellous(Value1,Value2):
    Ans1 =Add(Value1,Value2)
    
    Ans2 =Sub(Value1,Value2)

    return Ans1,Ans2
     
def main():
    Arr= Marvellous(11,6)
    print("Addition:",Arr[0])
    print("Substraction:",Arr[1])


if __name__=="__main__":
    main()