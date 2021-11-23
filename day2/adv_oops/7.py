class sample:
    ca = 100
    cb = 200

    def funca():
        la = 100
        lb = 200
        return dir()

for k, v in sample.__dict__.items():
    print(k,":", v)
    print("---")
