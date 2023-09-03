import multiprocessing
import os

def Task1(value):
    print("Executing the first task...")
    print("PID of running process for task1 :",os.getpid())
    print("PID of Parent process for task1 :",os.getppid())

def Task2(value):
    print("Executing the second task...")
    print("PID of running process for task2 :",os.getpid())
    print("PID of Parent process for task2 :",os.getppid())
    
def main():
    print("Demostration of Multiprocessing")


    print("PID of running process is:",os.getpid())

    no = 5
    p1=multiprocessing.Process(target= Task1, args=(no,))
    p2=multiprocessing.Process(target= Task2, args=(no,))

    p1.start()
    p2.start()

    p1.join()  # main/Parent funtion will wait untill execution of P1/child
    p2.join()
  
if __name__ == "__main__":
    main()