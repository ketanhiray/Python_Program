import threading

def Forward_Numbers():
    for i in range (1,51):
        print("Thread1:",i)
    print("Thread- 1 Completed")

def Reverse_Number():
    for i in range (50,0,-1):
        print("Thread2",i)
    print("Thread- 2 Completed ")


t1= threading.Thread(target=Forward_Numbers)
t2= threading.Thread(target=Reverse_Number)


t1.start()
t1.join()

t2.start()


#t2.join()


