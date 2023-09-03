
Power=lambda No : 2 ** No

def main():
    
    print("Enter the number:")

    No =int(input())

    Ret =Power(No)

    print("Power is:",Ret)

   
if __name__ == "__main__":
    main()