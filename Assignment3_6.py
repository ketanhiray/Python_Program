import MarvellousNum

def main():
    
    print("Enter the number of elements that you want to store:")
    length = int(input())

    Arr = list()

    print("Enter the elements:")
    for i in range(length):
        value = int(input())
        Arr.append(value)


if __name__=="__main__":
    main()