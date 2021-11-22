class Bank:

    def __init__(self, an=0, ob=0, name="john doe"):
        self.accNum = an
        self.opnBal = ob
        self.curBal = self.opnBal
        self.cusName = name
        self.__rating = 0

    def display(self):
        print("welcome", self.cusName)
        print("account balance is", self.curBal)

    def withdraw(self, amt):
        if self.curBal > amt:
            self.curBal = self.curBal - amt
            self.display()
        else:
            print("not enough funds")

    def __calcRating(self):
    # criteria 1
    # criteria 2
    # criteria 3
        self.__rating = round(self.opnBal/1000, 1)    # rounding of 1 decimal


    def loan(self):
        self.__calcRating()
        if self.__rating > 0 and self.__rating < 2:
            print("you can get a loan of", self.__rating * 1000)
        elif self.__rating >= 2 and self.__rating < 4:
            print("you can get a loan of", self.__rating * 1500)
        else :
            print("you can get a loan of", self.__rating * 2000)


obja = Bank(45002, 2000, "Robert Downey")
objb = Bank(45004, 1400, "Chris Evans")

obja.loan()
print("-----")
objb.loan()
print("-----")

# error
print(obja.__rating)
