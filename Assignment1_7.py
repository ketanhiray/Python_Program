#Write a program which contains one function that accept one number from user and returns 
#true if number is divisible by 5 otherwise return false.
def CheckDiv():

   no= float(input("Enter number:"))

   if(no % 5 == 0):
    print("True")
   else:
    print("False")

def main():
   CheckDiv()

if __name__=="__main__":
    main()