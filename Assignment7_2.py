import threading

No= int(input("Enter the Number:"))

def EvenFactor(No):
    even_sum=0
    for i in range(2,No +1,2):
        if No % i == 0:
            even_sum += i
    
    print("Sum of Even numbers factors is:",even_sum)


def OddFactor(No):
    odd_sum =0
    for i in range(1,No + 1,2):
        if No % i == 0:
            odd_sum +=i
    print("Sum of Odd numbers factors is: ",odd_sum)

t1= threading.Thread(target=EvenFactor,args=(No,))
t2= threading.Thread(target=OddFactor,args=(No,))


t1.start()
t2.start()

t1.join()
t2.join()

print("Exit from main")



