class Bank:
    accNum = 0
    opnBal = 0
    curBal = opnBal
    cusName = "john Doe"

    def display(self):
        print("welcome", self.cusName)
        print("account balance is", self.curBal)

    def deposit_one(self, amt):
        self.curBal = self.curBal + amt

    @classmethod
    def deposit_two(cls, amt):
        self.opnBal = cls.curBal = amt

obja = Bank()

obja.display()
print("-----")
obja.deposit_one(500)
obja.display()
print("-----")
obja.deposit_two(1000)

objb = Bank()
objb.display()
