import threading
import os

def Task1(value):
  print("PID of Task1 is:",os.getpid())
  print("Thread ID of First thread is :",threading.current_thread())


def Task2(value):
  print("PID of Task2 is :",os.getpid())
  print("Thread ID of Second thread is :",threading.current_thread())


def main():
    print("PId of Parent process is:",os.getpid())
    print("Thread ID of Main thread is :",threading.current_thread())
    no=5
    t1= threading.Thread(target=Task1,args=(no,))
    t2= threading.Thread(target=Task2,args=(no,))


    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__== "__main__":
    main()