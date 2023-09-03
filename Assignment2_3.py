#Write a program which accept one number from user and return its factorial.

def main():
   
    no= int(input("Enter No:"))
    value=1
    for i in range(1,no+1):
          value= value*i
    print("Factorial is:",value)

if __name__== "__main__":
    main()