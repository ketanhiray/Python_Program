class BankAccount:
    ROI =10.5  # clas variable
    
    def __init__(self): # constructor
        #self.AccountHolder =Name
        #self.Balance =Amount  # instance varible
        self.Name = input("Enter your name: ")
        self.Amount = float(input("Enter the initial amount in your account: "))

    def DisplayBalance(self): # instance mehtod
        print("Hello",self.Name)
        print("Your account balace is:",self.Amount)
    
    def Deposit(self,DepositAmount):
         self.Amount += DepositAmount
         print("Amount deposited successfully")  

    def Withdraw(self,WithdrawAmount): #instance mehtod
        if self.Amount < WithdrawAmount:
            print(" There is no sufficient balance")
        else:

            self.Amount=self.Amount - WithdrawAmount
            print("Amount Withdraw Successfully..")
   
    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        print(f"Interest earned at {BankAccount.ROI}% rate: {interest:.2f}")
    
def main():
    print("ROI of HDFC bank is:",BankAccount.ROI)
    
    #print("Creating new account...")
    Obj1 =BankAccount() 

    Obj2 = BankAccount() 

    Obj1.DisplayBalance()

    Obj2.DisplayBalance()
   
    print("Performing operation on Obj1")
    Obj1.Deposit(2000)
    Obj1.DisplayBalance()

    Obj1.Withdraw(1000)
    Obj1.DisplayBalance()

    print("Performing operation on Obj2")
    Obj2.Deposit(4000)
    Obj2.DisplayBalance()

    Obj2.Withdraw(500)
    Obj2.DisplayBalance()
    
    print("Calculate Intrest")

    Obj1.CalculateInterest()
    Obj2.CalculateInterest()

    Obj1.DisplayBalance()
    Obj2.DisplayBalance()

if __name__=="__main__":
    main()