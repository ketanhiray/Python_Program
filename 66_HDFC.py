class HDFC:
    ROI =9.5  # clas variable

    @classmethod
    def DispalyBankInfo(cls): # class method
        print("Welcome to HDFC bank portal")
        print("our bank is pvt ltd bank")
        print("We provide the rate of intrest on saving account is:",cls.ROI)
    
    @staticmethod
    def DisplayKYCInfo():
        print("According to the rules of RBI you should provide below documnet for KYC")
        print("Your Addhar card")
        print("Your PAN card")
        print("Your Passport size photo")
    
    def __init__(self,Name,Amount): # constructor
        self.AccountHolder =Name
        self.Balance =Amount  # instance varible
        print("Welcome",self.AccountHolder)
        print("Account gets Successfully created with initial balance:",self.Balance)

    def DisplayBalance(self): # instance mehtod
        print("Hello",self.AccountHolder)
        print("Your account balace is:",self.Balance)
    
    def Withdraw(self,Amount): #instance mehtod
        if self.Balance < Amount:
            print(" There is no sufficient balance")
        else:

            self.Balance=self.Balance -Amount
            print("Amount Withdraw Successfully..")

    def Deposit(self,Amount):
        self.Balance=self.Balance + Amount
        print("Amount deposited successfully")   

def main():
    print("ROI of HDFC bank is:",HDFC.ROI)
    
    HDFC.DispalyBankInfo()

    HDFC.DisplayKYCInfo()

    print("Creating new account...")
    Amit =HDFC("Amit",5000) #__init__(100,"Amit",5000)

    print("Creating new account...")
    Sagar = HDFC("Sagar",3000)
   
    print("Performing operation on Amit")
    Amit.Deposit(2000)
    Amit.DisplayBalance()

    Amit.Withdraw(1000)
    Amit.DisplayBalance()

    print("Performing operation on Sagar")
    Sagar.Deposit(4000)
    Sagar.DisplayBalance()

    Sagar.Withdraw(500)
    Sagar.DisplayBalance()
    

if __name__=="__main__":
    main()