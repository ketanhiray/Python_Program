def DisplayStar():

    no= int(input("Enter number:"))

    for i in range(1,no+1):
       for j in range(1,no+1):
        if j <= i:
            print(i,end =' ')
        else:
           print(j,end =' ')
       print()

def main():
    DisplayStar()

if __name__=="__main__":
    main()