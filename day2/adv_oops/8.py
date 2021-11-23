class sample:
    ca = 100
    cb = 200
    __cc = 300

    def funca():
        la = 100
        lb = 200

objs = sample()

for x in dir(objs):
    print(x)
