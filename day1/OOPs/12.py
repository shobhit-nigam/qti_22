class Bank:

    def __init__(self, an=0, ob=0, name="john doe"):
        self.accNum = an
        self.opnBal = ob
        self.curBal = self.opnBal
        self.cusName = name

    def display(self):
        print("welcome", self.cusName)
        print("account balance is", self.curBal)

    def withdraw(self, amt):
        if self.curBal > amt:
            self.curBal = self.curBal - amt
            self.display()
        else:
            print("not enough funds")


obja = Bank(45002, 2000, "Robert Downey")
objb = Bank()

obja.withdraw(500)
print("-----")
objb.withdraw(500)
