def main():
    no= int(input("Enter No:"))
    p = 0
    for i in range(2, no):
            if(no % i)==0:
                p=1
                break
    if p == 1:
        print("It's not Prime No.")         
    else:
        print("It's prime No.")
    

if __name__== "__main__":
    main()