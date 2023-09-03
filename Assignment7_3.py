import threading

def Even_list_sum(No):
    even_sum =sum(num for num in No if num % 2 == 0)
    print("Even list sum:",even_sum)

def Odd_list_sum(No):
    odd_sum =sum(num for num in No if num % 2 != 0)
    print("Odd list sum:",odd_sum)



if __name__ == "__main__":
   NumberList=[1,2,3,4,5,6,7,8,9,10]

t1= threading.Thread(target=Even_list_sum,args=(NumberList,))
t2= threading.Thread(target=Odd_list_sum,args=(NumberList,))


t1.start()
t2.start()

t1.join()
t2.join()

print("Both are threads have completed")

