from functools import reduce
def CheckNo(No):
    if((No>=70) and (No<=90)):
        return True
    else:
        return False

def Increase(No):
    return No+10

def Product(A,B):
        return A * B

def main():
    Data= []
    print("Enter the number of elemets:")

    Size =int(input())

    print("Enter the number:")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)
      

    print("Input List=",Data)

    output = list(filter(CheckNo,Data))
    print("List after filter =",output)

    moutput= list(map(Increase,output))

    print("List after map =",moutput)

    result =reduce(Product,moutput)
    print("Output of reduce =",result)
   
if __name__ == "__main__":
    main()