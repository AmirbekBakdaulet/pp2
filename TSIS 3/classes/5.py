class bank_account:
    def __init__(self,owner, balance):
        self.owner=owner
        self.balance=balance
    def deposit(self,depos):
        self.balance+=depos
        print(f"Deposit of {depos} accepted.New balance is {self.balance}")
    def withdraw(self,withdr):
        if withdr<= self.balance:
            self.balance-=withdr
            print(f"withdrawal of {withdr} substructed. New balance is {self.balance}")
        else:
            print("insufficient funds")
owner=int(input("owner is: "))
balance=int(input("balance is:" ))
acc=bank_account(owner,balance)
depos=int(input("amount of deposit: "))
acc.deposit(depos)
withdr=int(input("amount of withdrawal: "))
acc.withdraw(withdr)