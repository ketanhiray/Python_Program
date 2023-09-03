
def DisplayStar():

    no= int(input("Enter number:"))
   
    for i in range(no,0,-1):
    
        for j in range(1,i+1):
          print('*',end =' ')
        print()


def main():
    DisplayStar()

if __name__=="__main__":
    main()