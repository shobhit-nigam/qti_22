class Bank:
    accNum = 0
    opnBal = 0
    curBal = opnBal
    cusName = "john Doe"

    def display(self):
        print("welcome", self.cusName)
        print("account balance is", self.curBal)

#   instance nethod
    def deposit_one(self, amt):
        self.curBal = self.curBal + amt

    @classmethod
    def deposit_two(cls, amt):
        self.opnBal = cls.curBal = amt

    @staticmethod
    def water_cooler():
        print("have some water")

obja = Bank()
obja.water_cooler()
