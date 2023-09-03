#Write a program which display first 10 even numbers on screen.

def DisplayEvenNo():
  No=21
  for i in range(No):
    if  i%2==0:
        print(i)

def main():
    DisplayEvenNo()

if __name__=="__main__":
    main()