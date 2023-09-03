#Write a program which contains one function named as Add() which accepts two numbers 
#from user and return addition of that two numbers.

def Add():
    no1= int(input("Enter 1st Number:"))
    no2= int(input("Enter 2nd Number:"))
    sum= no1 + no2
    print("Addition of two numbers is:",sum)


def main():
    Add()

if __name__ == "__main__":
    main()