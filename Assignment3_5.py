import MarvellousNum

def main():
    
    print("Enter the number of elements that you want to store:")
    length = int(input())

    Arr = list()

    print("Enter the elements:")
    for i in range(length):
        value = int(input())
        Arr.append(value)

    ansList = []
    for num in Arr:
        if num == 0 or num == 1 :
             continue    
        
        for i in range(2, num // 2 + 1) :
            if num % i == 0 :
               break
        else :    
             ansList.append(num)

    if len(ansList) :
       print("Prime Numbers : ",end = "-> ")
       for ans in ansList :
          print(ans, end = ", ")
    
          #print("Addition of Elements is:", sum([i for i in ans])) 

    else :
       print("No any number from the given list is Prime")

if __name__=="__main__":
    main()