from functools import reduce
def CheckEven(No):
    if(No % 2) == 0:
       
        return True
    else:
        return False

def Square(No):
    return pow(No,2)

def Add(A,B):
        return A + B

def main():
    Data= []
    print("Enter the number of elemets:")

    Size =int(input())

    print("Enter the number:")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)
      

    print("Input List=",Data)

    output = list(filter(CheckEven,Data))
    print("List after filter =",output)

    moutput= list(map(Square,output))

    print("List after map =",moutput)

    result =reduce(Add,moutput)
    print("Output of reduce =",result)
   
if __name__ == "__main__":
    main()