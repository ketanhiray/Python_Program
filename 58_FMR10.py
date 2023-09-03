#import userModuleforFMR

from userModuleforFMR import filterX
from userModuleforFMR import mapX
from userModuleforFMR import reduceX

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

    output = list(filterX(CheckEven,Data))
    print("Output after filter:",output)

    moutput= list(mapX(Increase,output))

    print("Output After Map:",moutput)

    result =reduceX(Add,moutput)
    print("Output After Reduce:",result)
   
if __name__ == "__main__":
    main()