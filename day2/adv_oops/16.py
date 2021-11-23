class time:
    def __new__(cls, x, y):
        print("creating instance")

    def __init__(self, h=0, m=0):
        print("init is called")
        self.hours = h
        self.minutes = m

    def display(self):
        print(f"{self.hours} hours and {self.minutes} minutes")

sat = time(0, 55)
sun = time(1, 35)
