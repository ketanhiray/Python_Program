
#Funtion define another funtion inside it and return as it's return value

def Demo(): # 200
    def Add(A,B): #100
        return A+B    
  
    return Add   #100

def main():      #300
    Ret= Demo()   # 200
    Ans= Ret(11,7) #100(11,7)
    print("Addition is:",Ans)

if __name__=="__main__":
    main() #0X300()