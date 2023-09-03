from functools import reduce

CheckEven = lambda No: No % 2 == 0
 
Increase= lambda No :No+2

Add= lambda A,B :A + B


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
    print("Output after filter:",output)

    moutput= list(map(Increase,output))

    print("Output After Map:",moutput)

    result =reduce(Add,moutput)
    print("Output After Reduce:",result)
   
if __name__ == "__main__":
    main()