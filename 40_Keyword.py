def Display(name,age,marks):
    print("Name:",name)
    print("age:",age)
    print("marks:",marks)


def main():
    print("Demostration of Keyword argument")

    Display(name="Ketan",age=30,marks=90)

    Display(name="Pallavi",age=28,marks=80)

if __name__=="__main__":
    main()