
#Funtion accept more Parameter and return parameters
def Marvellous(Value1,Value2):
    if(Value1>Value2):
        return Value1
    else:

        return Value2
    
     
def main():
    Ret =Marvellous(78,45)
    print("Largest no. is:",Ret)

    Ret=Marvellous(34,99)
    print("Largest no. is:",Ret)
   

if __name__=="__main__":
    main()