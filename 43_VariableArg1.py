def Display(*Values):
    for i in range(len(Values)):
     print(Values[i])

def main():
    print("Demostration of keyword argument")

    Display(10,20,30,40,50,60)
    Display(77,55,66)

if __name__=="__main__":
    main()