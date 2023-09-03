from functools import reduce
def CheckPrime(No):
    if No < 2:
        return False
    i = 2
    while i*i <= No:
        if No % i == 0:
            return False
        i += 1
    return True

def Multi(No):
    return No * 2

def Max(A,B):
        return max(A,B)

def main():
    Data= []
    print("Enter the number of elemets:")

    Size =int(input())

    print("Enter the number:")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)
      

    print("Input List=",Data)

    output = list(filter(CheckPrime,Data))
    print("List after filter =",output)

    moutput= list(map(Multi,output))

    print("List after map =",moutput)

    result =reduce(max,moutput)
    print("Output of reduce =",result)
   
if __name__ == "__main__":
    main()