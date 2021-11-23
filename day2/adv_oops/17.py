class time:
    def __new__(cls, h=10, m=20):
        print("creating instance")
        return super(time, cls).__new__(cls)

    def __init__(self, h=0, m=0):
        print("init is called")
        self.hours = h
        self.minutes = m

    def display(self):
        print(f"{self.hours} hours and {self.minutes} minutes")

objs = time()

objs.display()
