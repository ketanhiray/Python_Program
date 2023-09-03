def ChkPrime(Arr,ans):
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
     
    else :
       print("No any number from the given list is Prime")


