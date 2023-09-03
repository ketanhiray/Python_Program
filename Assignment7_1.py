import threading


def Even_Numbers():
    for i in range(2,21,2):
        print(f"Even Numbers:{i}")


def Odd_Numbers():
    for i in range(1,20,2):
        print(f"Odd Numbers: {i}")


even_thread = threading.Thread(target=Even_Numbers)
odd_thread= threading.Thread(target=Odd_Numbers)


even_thread.start()
odd_thread.start()

even_thread.join()
odd_thread.join()



