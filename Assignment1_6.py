#Write a program which accept number from user and check whether that number is positive or 
#negative or zero

def CheckNumber():

    no= float(input("Enter No:"))

    if no>0:
        print("Number is Positive")
    elif no == 0:
        print("Number is Zero")
    else:
        print("Number is Negetive")

def main():
    CheckNumber()

if __name__ == "__main__":
    main()