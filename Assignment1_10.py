#Write a program which accept name from user and display length of its name.

def DisplayLength():
    name= input("Enter Name:")

    length=len(name)
    print(length)

def main():
    DisplayLength()

if __name__=="__main__":
    main()