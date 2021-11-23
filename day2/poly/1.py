ia = 70

print("type of ia =", type(ia))

ia = "hello"
print("type of ia =", type(ia))

def funca():
    print("no parameters")

print("----")
funca()

def funca(la, lb):
    print("two parameters")

print("----")
# error
funca()
