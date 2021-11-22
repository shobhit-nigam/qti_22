class Bank:
    accNum = 0
    opnBal = 0
    curBal = opnBal
    cusName = "john Doe"

    def __init__(self):
        print("hello from init")

    def display(self):
        print("welcome", self.cusName)
        print("account balance is", self.curBal)

    def update(self, an, ob, name):
        self.accNum = an
        self.opnBal = ob
        self.curBal = self.opnBal
        self.cusName = name

obja = Bank()
objb = Bank()

print("----")

obja.update(45002, 2000, "Robert Downey")

obja.display()
print("-----")
objb.display()
