import threading

def small_ch_count(s):
    count =sum(1 for char in s if char.islower())
    print(f"Small Thread (ID : {threading.get_ident()},Name: {threading.current_thread().name}) - Small Charactes count is: {count}")

def capital_ch_count(s):
    count =sum(1 for char in s if char.isupper())
    print(f"Capital Thread (ID:{threading.get_ident()},Name:{threading.current_thread().name}) - Capital Characters count is: {count} ")


def digits_count(s):
    count =sum(1 for char in s if char.isdigit())
    print(f"Digit Thread (ID:{threading.get_ident()},Name:{threading.current_thread().name})- Digit count is: {count}")

if __name__=="__main__":
    input_string= "Marvellous System 123"


t1= threading.Thread(target=small_ch_count,args=(input_string,))
t2= threading.Thread(target=capital_ch_count,args=(input_string,))
t3= threading.Thread(target=digits_count,args=(input_string,))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()


print("All threads have completed")