#4.Write a program which accept one number form user and return addition of its factors.

def main():
    no= int(input("Enter No:"))
  
    add = 0

    for i in range(1,no + 1):
        if no%i== 0:
            add= add+i

    print("Addition of Factorial is:",add)

if __name__== "__main__":
    main()