class BankAccount:
    ##class variable
    interest_rate = 0.05
    
    #### instance variable 
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0
        
    def deposit(self , amount):
        ##### adding amount to balance
        if amount > 0:
            self.balance += amount
            
            ##subtracting amount from balance
    def withdraw(self,amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            
            ###### adding interest to balance
    def apply_interest(self):
        self.balance += self.balance * BankAccount.interest_rate
        
        
    ##### displaying account holders and their balance
    def display_account_info(self):
        print(f"Account_holder: {self.account_holder}, balance: shs{self.balance: .2f}")
        
if __name__ == "__main__":
    ######### creating the accounts
        account1 = BankAccount("Nicholas")
        account2 = BankAccount("Kemirembe")
       #### performing desposits for both accounts
        account1.deposit(100000)
        account2.deposit(200000)
        ### performing withdraw for both accounts
        account1.withdraw(5000)
        account2.withdraw(50000)
        ##### apply interest for both accounts
        account1.apply_interest()
        account2.apply_interest()
        #### display account information
        account1.display_account_info()
        account2.display_account_info()