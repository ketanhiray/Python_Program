from functools import reduce

def CheckEven(No):
    return (No % 2 == 0)
    

def Increase(No):
    return No+2

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
      
    #Data= [5,4,9,8,13,17,12,18]
    print("Given numbers:",Data)

    output = list(filter(CheckEven,Data))
    print(output)

    moutput= list(map(Increase,output))

    print(moutput)

    result =reduce(Add,moutput)
    print(result)
   
if __name__ == "__main__":
    main()