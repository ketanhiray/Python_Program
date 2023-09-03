import time

def fun(no):
    sum=0
    for i in range(100000):
        sum=sum+(no*no)
    return sum
def main():
    print("Demostration of serial execution using single core")
    
    starttime=time.time()

    Result =[]

    for no in range(10000):
        Result.append(fun(no))

    endtime= time.time()

    print("Time required to execute the application is:",endtime-starttime)
if __name__=="__main__":
    main()