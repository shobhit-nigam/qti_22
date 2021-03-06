class time:
    def __init__(self, h=0, m=0):
        self.hours = h
        self.minutes = m

    def display(self):
        print(f"{self.hours} hours and {self.minutes} minutes")

    def __add__(self, other):
        temp = time()
        if type(other) is time:
            tot_min = self.minutes + self.hours*60 + other.minutes + other.hours*60
            temp.hours = tot_min//60
            temp.minutes = tot_min%60

        elif type(other) is int:
            tot_min = self.minutes + self.hours*60 + other
            temp.hours = tot_min//60
            temp.minutes = tot_min%60

        else:
            print("some error message")

        return temp

    def __radd__(self, other):
        temp = time()

        if type(other) is int:
            tot_min = self.minutes + self.hours*60 + other
            temp.hours = tot_min//60
            temp.minutes = tot_min%60

        elif type(other) is tuple:
            tot_min = self.minutes + self.hours*60 + other[0]*60 + other[1]
            temp.hours = tot_min//60
            temp.minutes = tot_min%60

        return temp

sat = time(0, 55)
sun = time(1, 35)
mon = time(1, 40)

total = 10 + sat
total.display()
print("----")
total = (1, 20) + sat
total.display()

"""
operator + (time, time)
operator + (time, int)
opertaor + (int, time)

friend
"""
