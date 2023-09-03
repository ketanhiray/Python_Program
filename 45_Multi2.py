import multiprocessing
import os

def Task1(value):
    print("Executing the first task...")
    for i in range(value):
        print ("Task1:",i)

def Task2(value):
    print("Executing the second task...")
    for i in range(value):
        print ("Task2:",i)

def main():
    print("Demostration of Multiprocessing")


  
    no1=5
    no2=8
    p1=multiprocessing.Process(target= Task1, args=(no1,))
    p2=multiprocessing.Process(target= Task2, args=(no2,))

    p1.start()
    p2.start()

    p1.join()  # main/Parent funtion will wait untill execution of P1/child
    p2.join()
  
if __name__ == "__main__":
    main()