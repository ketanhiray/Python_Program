
#Funtion accepts Parameters as another funtion
def Add(A,B): #0x00000299878C6020
    return A+B

#def Sub(A,B):
 #   return A-B

def Marvellous(FPTR1):
    print(type(FPTR1))
    print(FPTR1)
    Ans =FPTR1(11,7) # Ans =0x00000299878C6020(11,7)
    print("Addition is:",Ans)  
     
def main():
    Marvellous(Add) #Marvellous(0x00000299878C6020)
   

if __name__=="__main__":
    main()