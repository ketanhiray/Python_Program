def CheckEven(value):
    result=value %2

    if (result==0):
        print("No is Even")
    else:
        print("No is Old")

def main():
    print("Enter the No:")
    no=int(input())

    CheckEven(no)

if __name__ == "__main__":
    main()
