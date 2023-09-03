def Display(name,age,marks=90):
    print("Name:",name)
    print("age:",age)
    print("marks:",marks)


def main():
    print("Demostration of Keyword argument")

    Display("Ketan",30)

    Display("Pallavi",28,80)

if __name__=="__main__":
    main()