class time:
    def __init__(self, h=0, m=0):
        self.hours = h
        self.minutes = m

    def __repr__(self):
        return f"time({self.hours}, {self.minutes})"

    def __str__(self):
        return f"{self.hours} hours and {self.minutes} minutes"


sat = time(0, 55)
sun = time(1, 35)

# user, client
print(sat)

# log, internals team
print(repr(sat))
print(sat.__repr__())

# float() looks for __float__
# repr() looks for __repr__
