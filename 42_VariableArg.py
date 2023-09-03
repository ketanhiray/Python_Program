def Display(*Values):
    print(type(Values))
    print(len(Values))
    print(Values)

def main():
    print("Demostration of keyword argument")

    Display(10,20,30,40,50,60)

if __name__=="__main__":
    main()