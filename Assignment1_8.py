# Write a program which accept number from user and print that number of “*” on screen

def DisplayStart():

    no= int(input("Enter number:"))

    for i in range(0,no):
       print("*")

def main():
    DisplayStart()

if __name__=="__main__":
    main()