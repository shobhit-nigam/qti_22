class time:
    def __init__(self, h=0, m=0):
        print("init is called")
        self.hours = h
        self.minutes = m

    def display(self):
        print(f"{self.hours} hours and {self.minutes} minutes")

    def __del__(self):
        print("del is called")

sat = time(0, 55)
sun = time(1, 35)
"""
sat.display()
sun.display()
print("----")
del sat
sat.display()
sun.display()
"""
