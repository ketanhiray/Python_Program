#from functools import reduce
import functools

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

    output = list(filter(lambda No: No % 2 == 0,Data))
    print("Output after filter:",output)

    moutput= list(map(lambda No :No+2,output))

    print("Output After Map:",moutput)

    result =functools.reduce(lambda A,B :A + B,moutput)
    print("Output After Reduce:",result)
   
if __name__ == "__main__":
    main()