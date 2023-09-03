
#Funtion accept more Parameter and return nothing
def Marvellous(Name,Age,City):
    print("Inside marvellous function")
    print("Wlecome:",Name)
    print("Your age is:",Age)
    print("Your city is:",City)
     
def main():
    Marvellous("Amit",28,"pune")
    Marvellous(City="Mumbai",Age=30,Name="sagar")

if __name__=="__main__":
    main()