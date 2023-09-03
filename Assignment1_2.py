#Write a program which contains one function named as ChkNum() which accept one 
#parameter as number. If number is even then it should display “Even number” otherwise 
#display “Odd number” on console.

def ChkNum():
    No= int(input("Enter Number:"))
    if (No % 2) == 0:
        print("Even Number")
    else:
        print("Odd Number")

def main():
    ChkNum()
if __name__ == "__main__":
    main()