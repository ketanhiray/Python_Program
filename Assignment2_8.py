def DisplayStar():

    no= int(input("Enter number:"))

    for i in range(0,no):
       k=1
       for j in range(0,i+1):
        print(k,end =' ')
        k = k+1
       print()


def main():
    DisplayStar()

if __name__=="__main__":
    main()