def DisplayStar():

    no= int(input("Enter number:"))

    for i in range(no):
       for j in range(no):
        print('*',end =' ')
       print()


def main():
    DisplayStar()

if __name__=="__main__":
    main()