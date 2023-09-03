#1.Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub()
#for subtraction, Mult() for multiplication and Div() for division. All functions accepts two
#parameters as number and perform the operation. Write on python program which call all the
#functions from Arithmetic module by accepting the parameters from user.
import A_2_1_Arithmetic

def main():
    print("Enter the 1st number:")
    a= int(input())

    print("Enter the 2nd number:")
    b= int(input())

    print("Addition is:",A_2_1_Arithmetic.Add(a,b))
    print("Substraction is:",A_2_1_Arithmetic.Sub(a,b))
    print("Multiplication is:",A_2_1_Arithmetic.Mult(a,b))
    print("Divition is:",A_2_1_Arithmetic.Div(a,b))

if __name__ == "__main__":
    main()